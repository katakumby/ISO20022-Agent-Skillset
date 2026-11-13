---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 camt.004.001.10 ReturnAccountV10", "3.4 Message Building Blocks", "3.4.2 ReportOrError <RptOrErr>", "3.4.2.1 AccountReport <AcctRpt>", "3.4.2.1.2 AccountOrError <AcctOrErr>", "3.4.2.1.2.1 Account <Acct>", "3.4.2.1.2.1.10 StandingOrder <StgOrdr>", "3.4.2.1.2.1.10.11 LinkSetIdentification <LkSetId>"]
file_pages: [86]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.004.001.10"]
---

# 3.4.2.1.2.1.10.11 LinkSetIdentification <LkSetId>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 86 to 86.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 86

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
3.4.2.1.2.1.10.11  LinkSetIdentification <LkSetId>
Presence: [0..1]
Definition: Unique identification to unambiguously identify the link set in which the standing order is
defined. The link set is a collection of standing order defined in a specific sequence.
Datatype: "Max35Text" on page 889
3.4.2.1.2.1.10.12  LinkSetOrderIdentification <LkSetOrdrId>
Presence: [0..1]
Definition: Unique identification to unambiguously identify liquidity transfer standing order within the link
set.
Datatype: "Max35Text" on page 889
3.4.2.1.2.1.10.13  LinkSetOrderSequence <LkSetOrdrSeq>
Presence: [0..1]
Definition: Specifies the sequence in which the system will execute the liquidity transfers standing order
within the link set when additional liquidity is required.
Datatype: "Number" on page 886
3.4.2.1.2.1.10.14  ExecutionType <ExctnTp>
Presence: [0..1]
Definition: Defines whether the standing order is executed through a time-based or an event-based
trigger.
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 86 February 2025
```

