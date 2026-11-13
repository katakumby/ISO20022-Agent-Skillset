---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["7 reda.051.001.01 AccountLinkStatusAdviceV01", "7.4 Message Building Blocks", "7.4.2 AccountLinkStatus <AcctLkSts>", "7.4.2.2 StatusReason <StsRsn>", "7.4.2.2.1 Reason <Rsn>"]
file_pages: [51]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.051.001.01"]
---

# 7.4.2.2.1 Reason <Rsn>

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 51 to 51.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 51

```text
StatusReason <StsRsn> contains the following StatusReasonInformation10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  51
{Or     Code <Cd> [1..1] CodeSet 51
Or}     Proprietary <Prtry> [1..1] Text 51
   AdditionalInformation <AddtlInf> [0..1] Text 51
7.4.2.2.1  Reason <Rsn>
Presence: [1..1]
Definition: Specifies the reason for the status report.
Reason <Rsn> contains one of the following StatusReason6Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 51
Or}   Proprietary <Prtry> [1..1] Text 51
7.4.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the status, as published in an external reason code list.
Datatype: "ExternalStatusReason1Code" on page 74
7.4.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the status, in a proprietary form.
Datatype: "Max35Text" on page 78
7.4.2.2.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Further details on the status reason.
Usage: Additional information can be used for several purposes such as the reporting of repaired
information.
Datatype: "Max140Text" on page 77
7.4.3 AccountLinkIdentification <AcctLkId>
Presence: [0..1]
Definition: Provides a unique and unambiguous identification for the account link.
Impacted by: C3 "SecuritiesAccountOrBlockChainAddress1Rule", C4
"SecuritiesAccountOrBlockChainAddress2Rule", C5 "SecuritiesAccountOrBlockChainAddress3Rule"
Approved by the Securities SEG on 21 November 2024. reda.051.001.01 AccountLinkStatusAdviceV01
Target2-Securities - Link Reference Data 51 December 2024
```

