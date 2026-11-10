---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "18.4 Message Building Blocks", "18.4.3.9 ModificationRequested <ModReqd>"]
file_pages: [576, 577, 578, 579, 580, 581, 582]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.024.001.14"]
---

# 18.4.3.9 ModificationRequested <ModReqd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 576 to 582.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 576

```text
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
18.4.3.9  ModificationRequested <ModReqd>
Presence: [1..1]
Definition: Modification request from your counterparty for this transaction is pending waiting for your
cancellation request or your consent.
Impacted by: C3 "AdditionalReasonInforrmationRule"
ModificationRequested <ModReqd> contains the following elements (see "ProprietaryReason4" on
page 1899 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 1899
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1899
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
18.4.4 InferredMatchingStatus <IfrrdMtchgSts>
Presence: [0..1]
Definition: Provides the matching status of an instruction as per the account servicer based on an
allegement. At this time no matching took place on the market (at the Central Securities Depository
(CSD)/International Central Securities Depository (ICSD)).
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 576 March 2026
```

## File page 577

```text
InferredMatchingStatus <IfrrdMtchgSts> contains one of the following elements (see
"MatchingStatus24Choice" on page 1963 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Matched <Mtchd> [1..1] ± C1 1964
Or   Unmatched <Umtchd> [1..1]  1964
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1965
Or}     Reason <Rsn> [1..*]  1965
       Code <Cd> [1..1]  1965
{Or         Code <Cd> [1..1] CodeSet 1966
Or}         Proprietary <Prtry> [1..1] ± 1968
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1968
Or}   Proprietary <Prtry> [1..1] ± 1968
18.4.5 MatchingStatus <MtchgSts>
Presence: [0..1]
Definition: Provides the matching status of the instruction.
MatchingStatus <MtchgSts> contains one of the following elements (see "MatchingStatus24Choice"
on page 1963 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Matched <Mtchd> [1..1] ± C1 1964
Or   Unmatched <Umtchd> [1..1]  1964
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1965
Or}     Reason <Rsn> [1..*]  1965
       Code <Cd> [1..1]  1965
{Or         Code <Cd> [1..1] CodeSet 1966
Or}         Proprietary <Prtry> [1..1] ± 1968
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1968
Or}   Proprietary <Prtry> [1..1] ± 1968
18.4.6 SettlementStatus <SttlmSts>
Presence: [0..1]
Definition: Provides the status of settlement of a transaction.
Impacted by: C24 "PendingToFailingRule"
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 577 March 2026
```

## File page 578

```text
SettlementStatus <SttlmSts> contains one of the following elements (see
"SettlementStatus30Choice" on page 1952 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Pending <Pdg> [1..1] ± 1953
Or   Failing <Flng> [1..1] ± 1953
Or}   Proprietary <Prtry> [1..1] ± 1953
Constraints
• PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
18.4.7 TransactionDetails <TxDtls>
Presence: [0..1]
Definition: Identifies the details of the transaction.
Impacted by: C13 "InvestorCountryCodeRule", C26 "SafekeepingAccountOrBlockChainAddress1Rule",
C28 "SafekeepingAccountOrBlockChainAddress2Rule", C30
"SafekeepingAccountOrBlockChainAddress3Rule", C37 "TwoLegTransactionOpeningClosing1Rule",
C38 "TwoLegTransactionOpeningClosing2Rule"
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 578 March 2026
```

## File page 579

```text
TransactionDetails <TxDtls> contains the following TransactionDetails177 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeIdentification <TradId> [0..*] Text 583
   UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 583
   PoolIdentification <PoolId> [0..1] Text 584
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 584
   TripartyAgentServiceProviderCollateralTransactionId
entification <TrptyAgtSvcPrvdrCollTxId>
[0..1] Text 584
   ClientTripartyCollateralTransactionIdentification
<ClntTrptyCollTxId>
[0..1] Text 584
   ClientCollateralInstructionIdentification
<ClntCollInstrId>
[0..1] Text 584
   TripartyAgentServiceProviderCollateralInstructionIde
ntification <TrptyAgtSvcPrvdrCollInstrId>
[0..1] Text 584
   NonceIdentification <NonceId> [0..1] Text 584
   AccountOwner <AcctOwnr> [0..1] ± 585
   SafekeepingAccount <SfkpgAcct> [0..1] ± 585
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 585
   SafekeepingPlace <SfkpgPlc> [0..1] ± C31 585
   PlaceOfTrade <PlcOfTrad> [0..1] ± 586
   PlaceOfClearing <PlcOfClr> [0..1] ± 586
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C9, C10,
C14,
C15,
C19
586
   SettlementQuantity <SttlmQty> [1..1] ± 587
   PartiallyReleasedQuantity <PrtlyRlsdQty> [0..1] ± 588
   SettlementAmount <SttlmAmt> [0..1] ± 588
   DigitalPaymentSettlement <DgtlPmtSttlm> [0..1]  588
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C9, C10,
C14,
C15,
C19
589
     ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 590
     CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  590
{Or       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 590
Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C4 590
Or}       LEI <LEI> [1..1] IdentifierSet 591
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 579 March 2026
```

## File page 580

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LateDeliveryDate <LateDlvryDt> [0..1] ± 591
   ExpectedSettlementDate <XpctdSttlmDt> [0..1] ± 591
   ExpectedValueDate <XpctdValDt> [0..1] ± 591
   SettlementDate <SttlmDt> [1..1] ± 592
   TradeDate <TradDt> [0..1] ± 592
   AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 592
   MatchedStatusTimeStamp <MtchdStsTmStmp> [0..1] DateTime 592
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 593
   Payment <Pmt> [1..1] CodeSet 593
   SettlementParameters <SttlmParams> [1..1] ± C5, C33 593
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C20,
C21,
C22,
C23
594
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C20,
C21,
C22,
C23
596
   Investor <Invstr> [0..1] ± 597
   QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± 597
   SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
[0..1] Text 597
Constraints
• InvestorCountryCodeRule
If Investor is present with a country code, then the country code specifies the nationality of the
investor, for example, for the settlement of certain securities (that is, airlines, defence manufacturers)
under the EU legislation.
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
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 580 March 2026
```

## File page 581

```text
• SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
• TwoLegTransactionOpeningClosing1Rule
For settlement of two part transactions (Securities Financing), the opening/initiation and closing/
return of the transaction is confirmed by sending the following combination of
TransactionIdentificationDetails/SecuritiesMovementType codes and SettlementParameters/
SecuritiesTransactionType codes:
Repo Opening
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: Repo (REPU)
Repo Closing
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: Repo (REPU)
Reverse Repo Opening
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: ReverseRepo (RVPO)
Reverse Repo Closing
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: ReverseRepo (RVPO)
TriParty Repo Opening
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: TriPartyRepo (TRPO)
TriParty Repo Closing
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: TriPartyRepo (TRPO)
TriParty Reverse Repo Opening
SecuritiesMovementType: Receive (RECE)
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 581 March 2026
```

## File page 582

```text
SettlementParameters/SecuritiesTransactionType: TriPartyReverseRepo (TRVO)
TriParty Reverse Repo Closing
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: TriPartyReverseRepo (TRVO)
Securities Lending Initiation
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: SecuritiesLending (SECL)
Securities Lending Return
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: SecuritiesLending (SECL)
Securities Borrowing Initiation
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: SecuritiesBorrowing (SECB)
Securities Borrowing Return
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: SecuritiesBorrowing (SECB).
• TwoLegTransactionOpeningClosing2Rule
For settlement of two part transactions (buy-sell back, sell buy-back, collateral in and out), the
opening/initiation and closing/return of the transaction is identified by the providing of the following
combination of SecuritiesMovementType codes and SettlementParameters/
SecuritiesTransactionType codes:
Sell-Buy Back: Sell
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: SellBuyBack (SBBK)
Sell-Buy Back: Buy Back
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: SellBuyBack (SBBK)
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 582 March 2026
```

