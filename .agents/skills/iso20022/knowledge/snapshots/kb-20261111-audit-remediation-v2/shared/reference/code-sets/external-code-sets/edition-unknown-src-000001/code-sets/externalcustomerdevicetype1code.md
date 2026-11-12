---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalCustomerDeviceType1Code"]
code_set: "ExternalCustomerDeviceType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalCustomerDeviceType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalCustomerDeviceType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specified a type of customer device used for a card payment transaction.

External code sets can be downloaded from www.iso20022.org.
*`SECR`-Card reader device that meets security standards for encrypted PIN entry and secure transaction processing.
*`NSCR`-Card reader without advanced security features, typically used for low-risk or offline transactions.
*`MOBL`-Smartphone used for initiating or receiving transactions, often via apps or NFC.
*`TBLT`-Touchscreen tablet device functioning similarly to a mobile device for payments.
*`PECR`-Desktop or laptop computer used for online transactions through browsers or installed software.

*`OTHN`-Device type specific to a national payment scheme or infrastructure (such as proprietary POS terminals mandated by a country).
*`OTHP`-Proprietary device type used within a private network or closed-loop payment system.
*`WRBL`-Device worn on the body (such as fitness band, smart ring) that supports payment functionality.
*`VHCL`-In-vehicle system enabling payments (such as tolls, fuel, parking) through embedded technology.

*`EMBD`-Payment-enabled component integrated into another device or appliance.
*`KFOB`-Small portable device, often used for contactless payments.
*`JEWL`-Payment-enabled jewelry such as rings or bracelets with NFC or tokenization capabilities.
*`STIC`-Payment sticker with embedded NFC or RFID, typically attached to a physical object for tap-and-pay.
*`GAMB`-Console or gaming system that supports in-game or digital purchases.
*`WATC`-Smartwatch with payment capabilities.
*`UNKW`-Device type cannot be determined or is not disclosed.
*`TLVN`-Smart TV or connected device enabling payments for streaming or interactive services.
*`HDST`-Voice-activated device without a screen (e.g., smart speaker) used for initiating transactions.
*`IOTS`-Any IoT-enabled device capable of initiating or receiving payments (e.g., smart fridge ordering groceries).

## Source constraints

```json
{
  "type": "string",
  "minLength": 1,
  "maxLength": 4
}
```

## Complete enumeration

| Position | Exact code |
| --- | --- |
| 1 | SECR |
| 2 | NSCR |
| 3 | MOBL |
| 4 | TBLT |
| 5 | PECR |
| 6 | OTHN |
| 7 | OTHP |
| 8 | WRBL |
| 9 | VHCL |
| 10 | EMBD |
| 11 | KFOB |
| 12 | JEWL |
| 13 | STIC |
| 14 | GAMB |
| 15 | WATC |
| 16 | UNKW |
| 17 | TLVN |
| 18 | HDST |
| 19 | IOTS |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
