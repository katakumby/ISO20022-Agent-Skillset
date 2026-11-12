---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["6 reda.028.001.01 CollateralDataStatusAdviceV01", "6.4 Message Building Blocks", "6.4.2 StatusReason <StsRsn>", "6.4.2.2 Reason <Rsn>", "6.4.2.2.1 Reason <Rsn>", "6.4.2.2.1.1 Code <Cd>"]
file_pages: [41]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.028.001.01"]
---

# 6.4.2.2.1.1 Code <Cd>

Source: [src-000354](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 41 to 41.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 41

```text
Reason <Rsn> contains one of the following StatusReason6Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 41
Or}   Proprietary <Prtry> [1..1] Text 41
6.4.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the status, as published in an external reason code list.
Datatype: "ExternalStatusReason1Code" on page 80
6.4.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the status, in a proprietary form.
Datatype: "Max35Text" on page 83
6.4.2.2.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Further details on the status reason.
Usage: Additional information can be used for several purposes such as the reporting of repaired
information.
Datatype: "Max140Text" on page 83
6.4.3 StatusReasonAndFinancialInstrument
<StsRsnAndFinInstrm>
Presence: [0..1]
Definition: Specifies the reason for the status report per financial instrument and eligibility set.
Impacted by: C9 "StatusReasonRule"
Approved by the Securities SEG on 17 April 2025. reda.028.001.01 CollateralDataStatusAdviceV01
Target2-Securities - Collateral Management Reference Data 41 May 2025
```

