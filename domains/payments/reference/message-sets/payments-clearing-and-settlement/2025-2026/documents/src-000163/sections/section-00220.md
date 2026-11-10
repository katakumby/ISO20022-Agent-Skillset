---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.25 ReturnChain <RtrChain>"]
file_pages: [321, 322, 323]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.25 ReturnChain <RtrChain>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 321 to 323.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 321

```text
InstructedAgent <InstdAgt> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 1173 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  1174
     BICFI <BICFI> [0..1] IdentifierSet C5 1174
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1175
     LEI <LEI> [0..1] IdentifierSet 1175
     Name <Nm> [0..1] Text 1175
     PostalAddress <PstlAdr> [0..1] ± 1175
     Other <Othr> [0..1] ± 1176
   BranchIdentification <BrnchId> [0..1]  1177
     Identification <Id> [0..1] Text 1177
     LEI <LEI> [0..1] IdentifierSet 1177
     Name <Nm> [0..1] Text 1177
     PostalAddress <PstlAdr> [0..1] ± 1177
4.4.3.25  ReturnChain <RtrChain>
Presence: [0..1]
Definition: Provides all parties (agents and non-agents) involved in a return transaction.
Impacted by: C27 "IntermediaryAgent1AccountRule", C31 "IntermediaryAgent2AccountRule", C36
"IntermediaryAgent3AccountRule", C44 "PreviousInstructingAgent1AccountRule", C49
"PreviousInstructingAgent2AccountRule", C54 "PreviousInstructingAgent3AccountRule"
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
321 March 2026
```

## File page 322

```text
ReturnChain <RtrChain> contains the following TransactionParties11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UltimateDebtor <UltmtDbtr> [0..1]  324
{Or     Party <Pty> [1..1] ± 324
Or}     Agent <Agt> [1..1] ± 325
   Debtor <Dbtr> [1..1]  326
{Or     Party <Pty> [1..1] ± 326
Or}     Agent <Agt> [1..1] ± 327
   DebtorAccount <DbtrAcct> [0..1] ± C22,
C21
328
   InitiatingParty <InitgPty> [0..1]  329
{Or     Party <Pty> [1..1] ± 329
Or}     Agent <Agt> [1..1] ± 330
   DebtorAgent <DbtrAgt> [0..1] ± 331
   DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C22,
C21
332
   PreviousInstructingAgent1 <PrvsInstgAgt1> [0..1] ± 332
   PreviousInstructingAgent1Account
<PrvsInstgAgt1Acct>
[0..1] ± C22,
C21
333
   PreviousInstructingAgent2 <PrvsInstgAgt2> [0..1] ± 334
   PreviousInstructingAgent2Account
<PrvsInstgAgt2Acct>
[0..1] ± C22,
C21
334
   PreviousInstructingAgent3 <PrvsInstgAgt3> [0..1] ± 335
   PreviousInstructingAgent3Account
<PrvsInstgAgt3Acct>
[0..1] ± C22,
C21
336
   IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 337
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1] ± C22,
C21
337
   IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 338
   IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1] ± C22,
C21
339
   IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 340
   IntermediaryAgent3Account <IntrmyAgt3Acct> [0..1] ± C22,
C21
340
   CreditorAgent <CdtrAgt> [0..1] ± 341
   CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C22,
C21
342
   Creditor <Cdtr> [1..1]  343
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
322 March 2026
```

## File page 323

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or     Party <Pty> [1..1] ± 343
Or}     Agent <Agt> [1..1] ± 344
   CreditorAccount <CdtrAcct> [0..1] ± C22,
C21
345
   UltimateCreditor <UltmtCdtr> [0..1]  346
{Or     Party <Pty> [1..1] ± 346
Or}     Agent <Agt> [1..1] ± 347
Constraints
• IntermediaryAgent1AccountRule
If IntermediaryAgent1Account is present, then IntermediaryAgent1 must be present.
On Condition
    /IntermediaryAgent1 is absent
Following Must be True
    /IntermediaryAgent1Account Must be absent
• IntermediaryAgent2AccountRule
If IntermediaryAgent2Account is present, then IntermediaryAgent2 must be present.
On Condition
    /IntermediaryAgent2 is absent
Following Must be True
    /IntermediaryAgent2Account Must be absent
• IntermediaryAgent3AccountRule
If IntermediaryAgent3Account is present, then IntermediaryAgent3 must be present.
On Condition
    /IntermediaryAgent3 is absent
Following Must be True
    /IntermediaryAgent3Account Must be absent
• PreviousInstructingAgent1AccountRule
If PreviousInstructingAgent1Account is present, then PreviousInstructingAgent1 must be present.
On Condition
    /PreviousInstructingAgent1 is absent
Following Must be True
    /PreviousInstructingAgent1Account Must be absent
• PreviousInstructingAgent2AccountRule
If PreviousInstructingAgent2Account is present, then PreviousInstructingAgent2 must be present.
On Condition
    /PreviousInstructingAgent2 is absent
Following Must be True
    /PreviousInstructingAgent2Account Must be absent
• PreviousInstructingAgent3AccountRule
If PreviousInstructingAgent3Account is present, then PreviousInstructingAgent3 must be present.
On Condition
    /PreviousInstructingAgent3 is absent
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
323 March 2026
```

