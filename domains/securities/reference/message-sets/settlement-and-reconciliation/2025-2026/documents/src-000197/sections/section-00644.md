---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["28 sese.034.001.11 SecuritiesFinancingStatusAdviceV11", "28.4 Message Building Blocks", "28.4.6 RepoCallRequestStatus <RepoCallReqSts>"]
file_pages: [970, 971, 972, 973, 974]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.034.001.11"]
---

# 28.4.6 RepoCallRequestStatus <RepoCallReqSts>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 970 to 974.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 970

```text
28.4.5 SettlementStatus <SttlmSts>
Presence: [0..1]
Definition: Provides the status of settlement of a transaction.
Impacted by: C25 "PendingToFailingRule"
SettlementStatus <SttlmSts> contains one of the following elements (see
"SettlementStatus18Choice" on page 1882 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Pending <Pdg> [1..1] ± 1883
Or   Failing <Flng> [1..1]  1883
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1883
Or}     Reason <Rsn> [1..*]  1884
       Code <Cd> [1..1]  1884
{Or         Code <Cd> [1..1] CodeSet 1884
Or}         Proprietary <Prtry> [1..1] ± 1887
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1888
Or}   Proprietary <Prtry> [1..1] ± 1888
Constraints
• PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
28.4.6 RepoCallRequestStatus <RepoCallReqSts>
Presence: [0..1]
Definition: Provides the status of the repurchase agreement call request.
RepoCallRequestStatus <RepoCallReqSts> contains one of the following elements (see
"RepoCallRequestStatus7Choice" on page 1971 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1]  1972
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1972
Or}     Reason <Rsn> [1..*]  1972
       Code <Cd> [1..1] ± 1973
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1973
Or   Denied <Dnd> [1..1] ± 1973
Or}   Proprietary <Prtry> [1..1] ± 1973
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 970 March 2026
```

## File page 971

```text
28.4.7 TransactionDetails <TxDtls>
Presence: [0..1]
Definition: Identifies the details of the transaction.
Impacted by: C3 "AdditionalDetailsRule", C26 "SafekeepingAccountOrBlockChainAddress1Rule", C28
"SafekeepingAccountOrBlockChainAddress2Rule", C30
"SafekeepingAccountOrBlockChainAddress3Rule", C37 "TwoLegTransactionOpeningClosingRule"
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 971 March 2026
```

## File page 972

```text
TransactionDetails <TxDtls> contains the following SecuritiesFinancingTransactionDetails59
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesFinancingTradeIdentification
<SctiesFincgTradId>
[0..1] Text 975
   SecuritiesFinancingUniqueTransactionIdentifier
<SctiesFincgUnqTxIdr>
[0..1] IdentifierSet 975
   ClosingLegIdentification <ClsgLegId> [0..1] Text 975
   PoolIdentification <PoolId> [0..1] Text 975
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 975
   TripartyAgentServiceProviderCollateralTransactionId
entification <TrptyAgtSvcPrvdrCollTxId>
[0..1] Text 976
   ClientTripartyCollateralTransactionIdentification
<ClntTrptyCollTxId>
[0..1] Text 976
   AccountOwner <AcctOwnr> [0..1] ± 976
   SafekeepingAccount <SfkpgAcct> [0..1] ± 976
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 976
   SafekeepingPlace <SfkpgPlc> [0..1] ± C31 977
   PlaceOfTrade <PlcOfTrad> [0..1] ± 977
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C13,
C14,
C16,
C17,
C20
978
   SettlementQuantity <SttlmQty> [1..1] ± 979
   OpeningSettlementAmount <OpngSttlmAmt> [0..1] ± 979
   TerminationTransactionAmount <TermntnTxAmt> [0..1] ± 979
   DigitalPaymentSettlement <DgtlPmtSttlm> [0..1]  979
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C13,
C14,
C16,
C17,
C20
980
     ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 981
     CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  981
{Or       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 981
Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C6 981
Or}       LEI <LEI> [1..1] IdentifierSet 982
   OpeningSettlementDate <OpngSttlmDt> [1..1] ± 982
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 972 March 2026
```

## File page 973

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TerminationDate <TermntnDt> [0..1] ± 982
   TradeDate <TradDt> [0..1] ± 982
   ExpectedSettlementDate <XpctdSttlmDt> [0..1] ± 983
   ExpectedValueDate <XpctdValDt> [0..1] ± 983
   LateDeliveryDate <LateDlvryDt> [0..1] ± 983
   RateChangeDate <RateChngDt> [0..1] ± 984
   SecuritiesFinancingTransactionType
<SctiesFincgTxTp>
[1..1] CodeSet 984
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 984
   Payment <Pmt> [1..1] CodeSet 984
   SettlementParameters <SttlmParams> [0..1] ± C8, C33 985
   RateType <RateTp> [0..1] ± 986
   VariableRateSupport <VarblRateSpprt> [0..1] ± 986
   RepurchaseRate <RpRate> [0..1] ± C35 986
   StockLoanMargin <StockLnMrgn> [0..1] ± C35 987
   SecuritiesHaircut <SctiesHrcut> [0..1] ± C35 987
   PricingRate <PricgRate> [0..1] ± 987
   Spread <Sprd> [0..1] ± C35 988
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C7, C12,
C21,
C22,
C23,
C24,
C32
988
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C7, C12,
C21,
C22,
C23,
C24,
C32
990
   Investor <Invstr> [0..1] ± 992
   SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
[0..1] Text 993
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the sender and receiver, if
SettlementInstructionProcessingAdditionalDetails is present, then it must not contain information that
can be provided in a structured field.
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 973 March 2026
```

## File page 974

```text
• SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
• SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
• SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
• TwoLegTransactionOpeningClosingRule
For transactions settling in two legs (Securities Financing), the opening/initiation and closing/return
information of the transaction is provided by sending the following combination of
SecuritiesMovementType codes and SecuritiesFinancingTransactionType codes:
Repo Opening
SecuritiesMovementType: Delivery (DELI)
SecuritiesFinancingTransactionType: Repo (REPU)
Repo Closing
SecuritiesMovementType: Receive (RECE)
SecuritiesFinancingTransactionType: Repo (REPU)
Reverse Repo Opening
SecuritiesMovementType: Receive (RECE)
SecuritiesFinancingTransactionType: ReverseRepo (RVPO)
Reverse Repo Closing
SecuritiesMovementType: Delivery (DELI)
SecuritiesFinancingTransactionType: ReverseRepo (RVPO)
Securities Lending Initiation
SecuritiesMovementType: Delivery (DELI)
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 974 March 2026
```

