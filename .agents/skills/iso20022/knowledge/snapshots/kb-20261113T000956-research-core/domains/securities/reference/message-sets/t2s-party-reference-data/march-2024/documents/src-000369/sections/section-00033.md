---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["4 reda.016.001.01 PartyStatusAdviceV01", "4.4 Message Building Blocks", "4.4.2 PartyStatus <PtySts>", "4.4.2.2 StatusReason <StsRsn>", "4.4.2.2.1 Reason <Rsn>"]
file_pages: [39]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.016.001.01"]
---

# 4.4.2.2.1 Reason <Rsn>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 39 to 39.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 39

```text
StatusReason <StsRsn> contains the following StatusReasonInformation10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  39
{Or     Code <Cd> [1..1] CodeSet 39
Or}     Proprietary <Prtry> [1..1] Text 39
   AdditionalInformation <AddtlInf> [0..1] Text 39
4.4.2.2.1  Reason <Rsn>
Presence: [1..1]
Definition: Specifies the reason for the status report.
Reason <Rsn> contains one of the following StatusReason6Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 39
Or}   Proprietary <Prtry> [1..1] Text 39
4.4.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the status, as published in an external reason code list.
Datatype: "ExternalStatusReason1Code" on page 182
4.4.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the status, in a proprietary form.
Datatype: "Max35Text" on page 188
4.4.2.2.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Further details on the status reason.
Usage: Additional information can be used for several purposes such as the reporting of repaired
information.
Datatype: "Max140Text" on page 187
4.4.2.3  SystemPartyIdentification <SysPtyId>
Presence: [0..1]
Definition: Specifications of a party defined within a system.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.016.001.01 PartyStatusAdviceV01
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
39 March 2024
```

