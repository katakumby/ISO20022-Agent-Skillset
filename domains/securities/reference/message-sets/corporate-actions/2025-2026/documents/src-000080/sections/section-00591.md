---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.1 GeneralInformation <GnlInf>"]
file_pages: [773]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.1 GeneralInformation <GnlInf>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 773 to 773.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 773

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Balance <Bal> [1..1] ± 810
       PendingTransactions <PdgTxs> [0..*] ± 810
     PendingReceiptBalance <PdgRctBal> [0..*]  810
       Balance <Bal> [1..1] ± 811
       PendingTransactions <PdgTxs> [0..*] ± 811
   SupplementaryData <SplmtryData> [0..*] ± C23 811
14.4.3.5.1  GeneralInformation <GnlInf>
Presence: [1..1]
Definition: Provides general information related to a corporate action event.
GeneralInformation <GnlInf> contains the following EventInformation17 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 773
   OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 773
   EventType <EvtTp> [1..1] ± C13 773
   MandatoryVoluntaryEventType <MndtryVlntryEvtTp> [1..1] ± 774
   LastNotificationIdentification <LastNtfctnId> [0..1] ± 774
14.4.3.5.1.1  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [1..1]
Definition: Reference assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 1251
14.4.3.5.1.2  OfficialCorporateActionEventIdentification <OffclCorpActnEvtId>
Presence: [0..1]
Definition: Provides the reference of the linked official corporate action event.
Datatype: "Max35Text" on page 1251
14.4.3.5.1.3  EventType <EvtTp>
Presence: [1..1]
Definition: Type of corporate action event.
Impacted by: C13 "EventTypeRule"
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 773 February 2026
```

