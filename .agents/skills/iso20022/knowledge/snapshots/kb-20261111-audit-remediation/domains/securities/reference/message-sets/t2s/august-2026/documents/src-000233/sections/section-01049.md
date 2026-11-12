---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.3 Modify <Modfy>", "28.4.2.1.3.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.1.3.2.26 Confidential <Cnfdtl>"]
file_pages: [1520]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.3.2.26 Confidential <Cnfdtl>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1520 to 1520.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1520

```text
Definition: Indicates whether a security is interchangeable, ie, the security is allowed to be replaced by
another security, without loss of value.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
28.4.2.1.3.2.26  Confidential <Cnfdtl>
Presence: [0..1]
Definition: Indicates whether the details of the security are to be made available to the market, or kept
private between ICSDs and agency network.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
28.4.2.1.3.2.27  PrivatePlacement <PrvtPlcmnt>
Presence: [0..1]
Definition: The sale of securities directly to private persons, institutional investors, or both outside a
public offering. Such non-public deals (often without a publicly available prospectus) closing through the
ICSDs are placed directly with investors.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
28.4.2.1.3.2.28  ConvertibleIndicator <ConvtblInd>
Presence: [0..1]
Definition: Indicates whether the investor or the issuer has a conversion option.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
28.4.2.1.3.2.29  ConversionPeriod <ConvsPrd>
Presence: [0..1]
Definition: Period during which a convertible security may be converted according to the terms of the
issue.
ConversionPeriod <ConvsPrd> contains the following elements (see "DateTimePeriod1" on
page 2916 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 2916
   ToDateTime <ToDtTm> [1..1] DateTime 2916
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1520 August 2026
```

