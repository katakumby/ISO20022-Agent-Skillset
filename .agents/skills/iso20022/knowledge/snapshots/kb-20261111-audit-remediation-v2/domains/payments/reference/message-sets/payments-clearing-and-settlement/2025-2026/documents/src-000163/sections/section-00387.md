---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.24 UnderlyingFinancialInstitutionCreditTransfer <UndrlygFICdtTrf>"]
file_pages: [530, 531, 532, 533]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.24 UnderlyingFinancialInstitutionCreditTransfer <UndrlygFICdtTrf>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 530 to 533.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 530

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
4.4.3.27.24  UnderlyingFinancialInstitutionCreditTransfer <UndrlygFICdtTrf>
Presence: [0..1]
Definition: Provides information on the underlying financial institution credit transfer for which cover is
provided.
Impacted by: C10 "CreditorAgentAccountRule", C13 "DebtorAgentAccountRule", C29
"IntermediaryAgent1AccountRule", C30 "IntermediaryAgent1Rule", C33
"IntermediaryAgent2AccountRule", C35 "IntermediaryAgent2Rule", C38
"IntermediaryAgent3AccountRule", C40 "IntermediaryAgent3Rule", C46
"PreviousInstructingAgent1AccountRule", C51 "PreviousInstructingAgent2AccountRule", C53
"PreviousInstructingAgent2Rule", C56 "PreviousInstructingAgent3AccountRule", C58
"PreviousInstructingAgent3Rule", C48 "PreviousInstructingAgent1Guideline", C77
"UltimateCreditorGuideline", C79 "UltimateDebtorGuideline"
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
530 March 2026
```

## File page 531

```text
UnderlyingFinancialInstitutionCreditTransfer <UndrlygFICdtTrf> contains the following
CreditTransferTransaction82 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentIdentification <PmtId> [1..1] ± C74 534
   PaymentTypeInformation <PmtTpInf> [0..1] ± 535
   InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount C1, C11 535
   InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 536
   SettlementPriority <SttlmPrty> [0..1] CodeSet 536
   SettlementTimeIndication <SttlmTmIndctn> [0..1]  536
     DebitDateTime <DbtDtTm> [0..1] DateTime 536
     CreditDateTime <CdtDtTm> [0..1] DateTime 537
   SettlementTimeRequest <SttlmTmReq> [0..1] ± 537
   ExpiryDateTime <XpryDtTm> [0..1] DateTime 537
   PaymentSignature <PmtSgntr> [0..1]  537
{Or     ILPV4 <ILPV4> [1..1] Text 537
Or}     Signature <Sgntr> [1..1] Text 538
   PreviousInstructingAgent1 <PrvsInstgAgt1> [0..1] ± 538
   PreviousInstructingAgent1Account
<PrvsInstgAgt1Acct>
[0..1] ± C22,
C21
538
   PreviousInstructingAgent2 <PrvsInstgAgt2> [0..1] ± 539
   PreviousInstructingAgent2Account
<PrvsInstgAgt2Acct>
[0..1] ± C22,
C21
540
   PreviousInstructingAgent3 <PrvsInstgAgt3> [0..1] ± 541
   PreviousInstructingAgent3Account
<PrvsInstgAgt3Acct>
[0..1] ± C22,
C21
541
   InstructingAgent <InstgAgt> [0..1] ± 542
   InstructedAgent <InstdAgt> [0..1] ± 543
   IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 544
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1] ± C22,
C21
545
   IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 546
   IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1] ± C22,
C21
546
   IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 547
   IntermediaryAgent3Account <IntrmyAgt3Acct> [0..1] ± C22,
C21
548
   UltimateDebtor <UltmtDbtr> [0..1] ± 549
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
531 March 2026
```

## File page 532

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Debtor <Dbtr> [1..1] ± 549
   DebtorAccount <DbtrAcct> [0..1] ± C22,
C21
550
   DebtorAgent <DbtrAgt> [0..1] ± 551
   DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C22,
C21
551
   CreditorAgent <CdtrAgt> [0..1] ± 552
   CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C22,
C21
553
   Creditor <Cdtr> [1..1] ± 554
   CreditorAccount <CdtrAcct> [0..1] ± C22,
C21
554
   UltimateCreditor <UltmtCdtr> [0..1] ± 555
   InstructionForCreditorAgent <InstrForCdtrAgt> [0..*] ± 556
   InstructionForNextAgent <InstrForNxtAgt> [0..*]  556
     Code <Cd> [0..1] CodeSet 557
     InstructionInformation <InstrInf> [0..1] Text 557
   Purpose <Purp> [0..1] ± 557
   RemittanceInformation <RmtInf> [0..1] ± 557
   UnderlyingAllocation <UndrlygAllcn> [0..*]  C80 558
     Amount <Amt> [1..1] Amount C2, C12 558
     CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 559
     Account <Acct> [1..1] ± C22,
C21
559
     Purpose <Purp> [1..1] ± 559
     Reference <Ref> [1..1] Text 560
     RelatedReferences <RltdRefs> [0..*] ± 560
Constraints
• CreditorAgentAccountRule
If CreditorAgentAccount is present, then CreditorAgent must be present.
On Condition
    /CreditorAgent is absent
Following Must be True
    /CreditorAgentAccount Must be absent
• DebtorAgentAccountRule
If DebtorAgentAccount is present, then DebtorAgent must be present.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
532 March 2026
```

## File page 533

```text
On Condition
    /DebtorAgent is absent
Following Must be True
    /DebtorAgentAccount Must be absent
• IntermediaryAgent1AccountRule
If IntermediaryAgent1Account is present, then IntermediaryAgent1 must be present.
On Condition
    /IntermediaryAgent1 is absent
Following Must be True
    /IntermediaryAgent1Account Must be absent
• IntermediaryAgent1Rule
If IntermediaryAgent1 is present, then CreditorAgent must be present.
On Condition
    /IntermediaryAgent1 is present
Following Must be True
    /CreditorAgent Must be present
• IntermediaryAgent2AccountRule
If IntermediaryAgent2Account is present, then IntermediaryAgent2 must be present.
On Condition
    /IntermediaryAgent2 is absent
Following Must be True
    /IntermediaryAgent2Account Must be absent
• IntermediaryAgent2Rule
If IntermediaryAgent2 is present, then IntermediaryAgent1 must be present.
On Condition
    /IntermediaryAgent2 is present
Following Must be True
    /IntermediaryAgent1 Must be present
• IntermediaryAgent3AccountRule
If IntermediaryAgent3Account is present, then IntermediaryAgent3 must be present.
On Condition
    /IntermediaryAgent3 is absent
Following Must be True
    /IntermediaryAgent3Account Must be absent
• IntermediaryAgent3Rule
If IntermediaryAgent3 is present, then IntermediaryAgent2 must be present.
On Condition
    /IntermediaryAgent3 is present
Following Must be True
    /IntermediaryAgent2 Must be present
• PreviousInstructingAgent1AccountRule
If PreviousInstructingAgent1Account is present, then PreviousInstructingAgent1 must be present.
On Condition
    /PreviousInstructingAgent1 is absent
Following Must be True
    /PreviousInstructingAgent1Account Must be absent
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
533 March 2026
```

