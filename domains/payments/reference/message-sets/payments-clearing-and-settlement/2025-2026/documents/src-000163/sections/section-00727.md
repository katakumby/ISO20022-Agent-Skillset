---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.41 UnderlyingFinancialInstitutionCreditTransfer <UndrlygFICdtTrf>"]
file_pages: [983, 984, 985, 986]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.41 UnderlyingFinancialInstitutionCreditTransfer <UndrlygFICdtTrf>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 983 to 986.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 983

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
7.4.2.41  UnderlyingFinancialInstitutionCreditTransfer <UndrlygFICdtTrf>
Presence: [0..1]
Definition: Provides information on the underlying financial institution credit transfer for which cover is
provided.
Impacted by: C7 "CreditorAgentAccountRule", C11 "DebtorAgentAccountRule", C23
"IntermediaryAgent1AccountRule", C25 "IntermediaryAgent1Rule", C28
"IntermediaryAgent2AccountRule", C31 "IntermediaryAgent2Rule", C34
"IntermediaryAgent3AccountRule", C37 "IntermediaryAgent3Rule", C41
"PreviousInstructingAgent1AccountRule", C47 "PreviousInstructingAgent2AccountRule", C50
"PreviousInstructingAgent2Rule", C53 "PreviousInstructingAgent3AccountRule", C56
"PreviousInstructingAgent3Rule", C44 "PreviousInstructingAgent1Guideline", C74
"UltimateCreditorGuideline", C77 "UltimateDebtorGuideline"
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
983 March 2026
```

## File page 984

```text
UnderlyingFinancialInstitutionCreditTransfer <UndrlygFICdtTrf> contains the following
CreditTransferTransaction80 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentIdentification <PmtId> [1..1] ± C70 987
   PaymentTypeInformation <PmtTpInf> [0..1] ± 988
   InterbankSettlementAmount <IntrBkSttlmAmt> [1..1] Amount C1, C8 988
   InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 989
   SettlementPriority <SttlmPrty> [0..1] CodeSet 989
   SettlementTimeIndication <SttlmTmIndctn> [0..1]  989
     DebitDateTime <DbtDtTm> [0..1] DateTime 990
     CreditDateTime <CdtDtTm> [0..1] DateTime 990
   SettlementTimeRequest <SttlmTmReq> [0..1] ± 990
   ExpiryDateTime <XpryDtTm> [0..1] DateTime 990
   PaymentSignature <PmtSgntr> [0..1]  990
{Or     ILPV4 <ILPV4> [1..1] Text 991
Or}     Signature <Sgntr> [1..1] Text 991
   PreviousInstructingAgent1 <PrvsInstgAgt1> [0..1] ± 991
   PreviousInstructingAgent1Account
<PrvsInstgAgt1Acct>
[0..1] ± C16,
C15
991
   PreviousInstructingAgent2 <PrvsInstgAgt2> [0..1] ± 992
   PreviousInstructingAgent2Account
<PrvsInstgAgt2Acct>
[0..1] ± C16,
C15
993
   PreviousInstructingAgent3 <PrvsInstgAgt3> [0..1] ± 994
   PreviousInstructingAgent3Account
<PrvsInstgAgt3Acct>
[0..1] ± C16,
C15
994
   InstructingAgent <InstgAgt> [0..1] ± 995
   InstructedAgent <InstdAgt> [0..1] ± 996
   IntermediaryAgent1 <IntrmyAgt1> [0..1] ± 997
   IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1] ± C16,
C15
998
   IntermediaryAgent2 <IntrmyAgt2> [0..1] ± 999
   IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1] ± C16,
C15
999
   IntermediaryAgent3 <IntrmyAgt3> [0..1] ± 1000
   IntermediaryAgent3Account <IntrmyAgt3Acct> [0..1] ± C16,
C15
1001
   UltimateDebtor <UltmtDbtr> [0..1] ± 1002
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
984 March 2026
```

## File page 985

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Debtor <Dbtr> [1..1] ± 1002
   DebtorAccount <DbtrAcct> [0..1] ± C16,
C15
1003
   DebtorAgent <DbtrAgt> [0..1] ± 1004
   DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C16,
C15
1004
   CreditorAgent <CdtrAgt> [0..1] ± 1005
   CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C16,
C15
1006
   Creditor <Cdtr> [1..1] ± 1007
   CreditorAccount <CdtrAcct> [0..1] ± C16,
C15
1007
   UltimateCreditor <UltmtCdtr> [0..1] ± 1008
   InstructionForCreditorAgent <InstrForCdtrAgt> [0..*] ± 1009
   InstructionForNextAgent <InstrForNxtAgt> [0..*]  1009
     Code <Cd> [0..1] CodeSet 1010
     InstructionInformation <InstrInf> [0..1] Text 1010
   Purpose <Purp> [0..1] ± 1010
   RegulatoryReporting <RgltryRptg> [0..10] ± 1010
   RemittanceInformation <RmtInf> [0..1] ± 1011
   UnderlyingAllocation <UndrlygAllcn> [0..*]  C78 1011
     Amount <Amt> [1..1] Amount C2, C9 1012
     CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 1012
     Account <Acct> [1..1] ± C16,
C15
1013
     Purpose <Purp> [1..1] ± 1013
     Reference <Ref> [1..1] Text 1013
     RelatedReferences <RltdRefs> [0..*] ± 1014
Constraints
• CreditorAgentAccountRule
If CreditorAgentAccount is present, then CreditorAgent must be present.
On Condition
    /CreditorAgent is absent
Following Must be True
    /CreditorAgentAccount Must be absent
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
985 March 2026
```

## File page 986

```text
• DebtorAgentAccountRule
If DebtorAgentAccount is present, then DebtorAgent must be present.
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
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
986 March 2026
```

