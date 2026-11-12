---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.3 CommonFinancialInstrumentAttributes11", "13.1.6.3.24 Confidential <Cnfdtl>"]
file_pages: [356]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.3.24 Confidential <Cnfdtl>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 356 to 356.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 356

```text
Definition: Indicates whether a security is interchangeable, ie, the security is allowed to be replaced by
another security, without loss of value.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
• Meaning When True: Yes
• Meaning When False: No
13.1.6.3.24  Confidential <Cnfdtl>
Presence: [0..1]
Definition: Indicates whether the details of the security are to be made available to the market, or kept
private between ICSDs and agency network.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
• Meaning When True: Yes
• Meaning When False: No
13.1.6.3.25  PrivatePlacement <PrvtPlcmnt>
Presence: [0..1]
Definition: The sale of securities directly to private persons, institutional investors, or both outside a
public offering. Such non-public deals (often without a publicly available prospectus) closing through the
ICSDs are placed directly with investors.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
• Meaning When True: Yes
• Meaning When False: No
13.1.6.3.26  ConvertibleIndicator <ConvtblInd>
Presence: [0..1]
Definition: Indicates whether the investor or the issuer has a conversion option.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
• Meaning When True: Yes
• Meaning When False: No
13.1.6.3.27  ConversionPeriod <ConvsPrd>
Presence: [0..1]
Definition: Period during which a convertible security may be converted according to the terms of the
issue.
ConversionPeriod <ConvsPrd> contains the following elements (see "DateTimePeriod1" on page 237
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 237
   ToDateTime <ToDtTm> [1..1] DateTime 237
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 356 March 2024
```

