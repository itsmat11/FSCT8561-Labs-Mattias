
from pathlib import Path
from PIL import Image, ExifTags
import base64
import csv
import re
import xml.etree.ElementTree as ET


# Part 7A: Find the six PNG images

image_dir = Path("Images")
results = []

stages = (
    "RECON", "VULN", "EXPLOIT",
    "PERSIST", "LATERAL", "EXFIL"
)


# Part 7C: Identify messages using stage labels

def has_secret(text):
    return any(
        text.startswith(stage + ":")
        for stage in stages
    )


# Part 7C: Decode ASCII or Base64 messages

def decode_text(value):

    if isinstance(value, bytes):

        if value.startswith(b"ASCII\x00\x00\x00"):
            return (
                value[8:].decode("utf-8", errors="replace"),
                "EXIF ASCII"
            )

        return (
            value.decode("utf-8", errors="replace"),
            "plain text"
        )

    text = str(value).strip()

    # Check whether the text looks like Base64
    if (
        len(text) >= 16
        and len(text) % 4 == 0
        and re.fullmatch(r"[A-Za-z0-9+/]+={0,2}", text)
    ):

        try:
            decoded = base64.b64decode(
                text, validate=True
            ).decode("utf-8")

            if has_secret(decoded):
                return decoded, "Base64"

        except (ValueError, UnicodeDecodeError):
            pass

    return text, "plain text"


# Part 7C: Loop through each image

for image_path in sorted(image_dir.glob("*.png")):

    with Image.open(image_path) as img:

        fields = set(img.info.keys())
        candidates = []


        # Part 7C: Extract EXIF metadata

        exif = img.getexif()

        for tag_id, value in exif.items():

            tag = ExifTags.TAGS.get(
                tag_id, str(tag_id)
            )

            fields.add("EXIF/" + tag)

            if isinstance(value, (str, bytes)):
                candidates.append(
                    ("EXIF/" + tag, value)
                )


        # Part 7C: Check nested EXIF fields

        for tag_id, value in exif.get_ifd(34665).items():

            tag = ExifTags.TAGS.get(
                tag_id, str(tag_id)
            )

            fields.add("EXIF/" + tag)

            if isinstance(value, (str, bytes)):
                candidates.append(
                    ("EXIF/" + tag, value)
                )


        # Part 7C: Extract PNG text metadata

        for key, value in img.info.items():

            if (
                isinstance(value, str)
                and key not in ("xmp", "XML:com.adobe.xmp")
            ):

                candidates.append(
                    ("PNG text/" + key, value)
                )


        # Part 7C: Extract XMP metadata

        xmp = (
            img.info.get("XML:com.adobe.xmp")
            or img.info.get("xmp")
        )

        if xmp:

            if isinstance(xmp, bytes):
                xmp = xmp.decode(
                    "utf-8", errors="replace"
                )

            try:
                root = ET.fromstring(xmp)

                for element in root.iter():

                    if element.text and element.text.strip():

                        tag = element.tag.split("}")[-1]

                        fields.add("XMP/" + tag)

                        candidates.append(
                            ("XMP/" + tag, element.text.strip())
                        )

            except ET.ParseError:
                print("Could not parse XMP in", image_path.name)


        # Part 7C: Create the result fields

        suspected_field = ""
        raw_excerpt = ""
        encoding = ""
        recovered_message = ""
        risk_score = 0

        reason = "No stage-labeled message found by these checks."


        # Part 7C: Detect hidden messages and assign risk scores

        for field, raw in candidates:

            message, method = decode_text(raw)

            if has_secret(message):

                suspected_field = field
                raw_excerpt = str(raw)[:120]
                encoding = method
                recovered_message = message

                # Confirmed hidden message: +10
                risk_score = 10

                reason = "Stage-labeled hidden message found (+10)."

                # Base64 encoded message: +5
                if method == "Base64":

                    risk_score += 5

                    reason += " Base64 encoding required (+5)."

                # No additional points without separate evidence
                break


        # Part 7B: Save one result dictionary per image

        results.append({
            "filename": image_path.name,
            "format": img.format,
            "metadata_fields": ", ".join(sorted(fields)),
            "suspected_field": suspected_field,
            "raw_excerpt": raw_excerpt,
            "encoding": encoding,
            "recovered_message": recovered_message,
            "risk_score": risk_score,
            "reason": reason,
        })


# Part 7C: Export results to CSV

with open(
    "metadata_report.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=results[0].keys()
    )

    writer.writeheader()
    writer.writerows(results)


# Part 7C: Print scanner results

print("=== Metadata Scanner Results ===")

for row in results:

    print(
        row["filename"],
        "|",
        row["suspected_field"],
        "|",
        row["encoding"],
        "| Score:",
        row["risk_score"]
    )

    print(
        " Recovered:",
        row["recovered_message"]
    )


# Part 7C: Final summary

print()
print("Saved", len(results), "rows to metadata_report.csv")
