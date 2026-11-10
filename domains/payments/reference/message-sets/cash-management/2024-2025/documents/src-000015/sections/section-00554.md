---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["31 camt.070.001.06 ReturnStandingOrderV06", "31.4 Message Building Blocks", "31.4.2 ReportOrError <RptOrErr>", "31.4.2.1 Report <Rpt>", "31.4.2.1.2 StandingOrderOrError <StgOrdrOrErr>", "31.4.2.1.2.1 StandingOrder <StgOrdr>", "31.4.2.1.2.1.11 LinkSetIdentification <LkSetId>"]
file_pages: [726]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.070.001.06"]
---

# 31.4.2.1.2.1.11 LinkSetIdentification <LkSetId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 726 to 726.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 726

```text
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
ResponsibleParty <RspnsblPty> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 803 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  804
     BICFI <BICFI> [0..1] IdentifierSet C2 804
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 805
     LEI <LEI> [0..1] IdentifierSet 805
     Name <Nm> [0..1] Text 805
     PostalAddress <PstlAdr> [0..1] ± 805
     Other <Othr> [0..1] ± 806
   BranchIdentification <BrnchId> [0..1]  807
     Identification <Id> [0..1] Text 807
     LEI <LEI> [0..1] IdentifierSet 807
     Name <Nm> [0..1] Text 807
     PostalAddress <PstlAdr> [0..1] ± 807
31.4.2.1.2.1.11  LinkSetIdentification <LkSetId>
Presence: [0..1]
Definition: Unique identification to unambiguously identify the link set in which the standing order is
defined. The link set is a collection of standing order defined in a specific sequence.
Datatype: "Max35Text" on page 889
31.4.2.1.2.1.12  LinkSetOrderIdentification <LkSetOrdrId>
Presence: [0..1]
Definition: Unique identification to unambiguously identify liquidity transfer standing order within the link
set.
Datatype: "Max35Text" on page 889
31.4.2.1.2.1.13  LinkSetOrderSequence <LkSetOrdrSeq>
Presence: [0..1]
Definition: Specifies the sequence in which the system will execute the liquidity transfers standing order
within the link set when additional liquidity is required.
Datatype: "Number" on page 886
31.4.2.1.2.1.14  ExecutionType <ExctnTp>
Presence: [0..1]
Definition: Defines whether the standing order is executed through a time-based or an event-based
trigger.
Approved by the Payments SEG on 04 February 2025 camt.070.001.06 ReturnStandingOrderV06
Cash Management - Maintenance 2024 - 2025 726 February 2025
```

