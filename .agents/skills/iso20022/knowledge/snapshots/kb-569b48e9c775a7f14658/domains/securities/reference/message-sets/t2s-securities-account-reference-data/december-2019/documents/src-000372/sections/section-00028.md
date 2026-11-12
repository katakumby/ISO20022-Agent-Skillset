---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["4 reda.020.001.01 SecuritiesAccountStatusAdviceV01", "4.4 Message Building Blocks", "4.4.2 SecuritiesAccountStatus <SctiesAcctSts>", "4.4.2.3 StatusReason <StsRsn>"]
file_pages: [30, 31]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.020.001.01"]
---

# 4.4.2.3 StatusReason <StsRsn>

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 30 to 31.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 30

```text
4.4.2.3  StatusReason <StsRsn>
Presence: [0..*]
Definition: Reason for the status of a securities account maintenance instruction.
StatusReason <StsRsn> contains the following StatusReasonInformation10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  30
{Or     Code <Cd> [1..1] CodeSet 30
Or}     Proprietary <Prtry> [1..1] Text 30
   AdditionalInformation <AddtlInf> [0..1] Text 30
4.4.2.3.1  Reason <Rsn>
Presence: [1..1]
Definition: Specifies the reason for the status report.
Reason <Rsn> contains one of the following StatusReason6Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 30
Or}   Proprietary <Prtry> [1..1] Text 30
4.4.2.3.1.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the status, as published in an external reason code list.
Datatype: "ExternalStatusReason1Code" on page 95
4.4.2.3.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the status, in a proprietary form.
Datatype: "Max35Text" on page 100
4.4.2.3.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Further details on the status reason.
Usage: Additional information can be used for several purposes such as the reporting of repaired
information.
Datatype: "Max140Text" on page 99
4.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.020.001.01 SecuritiesAccountStatusAdviceV01
Target2-Securities - Securities Account Reference Data 30 December 2019
```

## File page 31

```text
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C3 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 84 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 84
   Envelope <Envlp> [1..1] (External Schema) 84
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.020.001.01 SecuritiesAccountStatusAdviceV01
Target2-Securities - Securities Account Reference Data 31 December 2019
```

