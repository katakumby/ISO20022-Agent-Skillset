---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["40 reda.020.001.01 SecuritiesAccountStatusAdviceV01", "40.4 Message Building Blocks", "40.4.2 SecuritiesAccountStatus <SctiesAcctSts>", "40.4.2.3 StatusReason <StsRsn>"]
file_pages: [2122, 2123]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.020.001.01"]
---

# 40.4.2.3 StatusReason <StsRsn>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2122 to 2123.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2122

```text
40.4.2.3  StatusReason <StsRsn>
Presence: [0..*]
Definition: Reason for the status of a securities account maintenance instruction.
StatusReason <StsRsn> contains the following StatusReasonInformation10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  2122
{Or     Code <Cd> [1..1] CodeSet 2122
Or}     Proprietary <Prtry> [1..1] Text 2122
   AdditionalInformation <AddtlInf> [0..1] Text 2122
40.4.2.3.1  Reason <Rsn>
Presence: [1..1]
Definition: Specifies the reason for the status report.
Reason <Rsn> contains one of the following StatusReason6Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2122
Or}   Proprietary <Prtry> [1..1] Text 2122
40.4.2.3.1.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the status, as published in an external reason code list.
Datatype: "ExternalStatusReason1Code" on page 3245
40.4.2.3.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the status, in a proprietary form.
Datatype: "Max35Text" on page 3328
40.4.2.3.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Further details on the status reason.
Usage: Additional information can be used for several purposes such as the reporting of repaired
information.
Datatype: "Max140Text" on page 3326
40.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.020.001.01 SecuritiesAccountStatusAdviceV01
Target2-Securities 2122 August 2026
```

## File page 2123

```text
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C3 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 3011 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 3011
   Envelope <Envlp> [1..1] (External Schema) 3012
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.020.001.01 SecuritiesAccountStatusAdviceV01
Target2-Securities 2123 August 2026
```

