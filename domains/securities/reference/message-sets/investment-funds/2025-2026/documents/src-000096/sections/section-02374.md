---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.28 SettlementAndCustodyDetails <SttlmAndCtdyDtls>"]
file_pages: [3339, 3340]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.28 SettlementAndCustodyDetails <SttlmAndCtdyDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3339 to 3340.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3339

```text
Constraints
• TaxElementRule
One of the elements (TaxableIncomePerDividend, EUCapitalGain, EUDividendStatus,
PercentageOfDebtClaim, IndividualTax) must be present.
52.4.5.10.28  SettlementAndCustodyDetails <SttlmAndCtdyDtls>
Presence: [0..1]
Definition: Parameters used to execute the settlement of an investment fund order.
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3339 May 2026
```

## File page 3340

```text
SettlementAndCustodyDetails <SttlmAndCtdyDtls> contains the following
FundSettlementParameters28 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementDate <SttlmDt> [0..1] Date 3341
   SettlementPlace <SttlmPlc> [1..1]  3341
     Party <Pty> [1..1]  3342
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C5 3342
Or       ProprietaryIdentification <PrtryId> [1..1] ± 3342
Or       NameAndAddress <NmAndAdr> [1..1] ± 3343
Or}       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3343
     LEI <LEI> [0..1] IdentifierSet 3343
   SafekeepingPlace <SfkpgPlc> [0..1] ± 3343
   SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 3344
   TradeTransactionCondition <TradTxCond> [0..*] ± 3344
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 3344
   ReceivingSideDetails <RcvgSdDtls> [0..1]  C36,
C37
3345
     ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  3346
       PartyIdentification <PtyId> [1..1] ± 3346
       AccountIdentification <AcctId> [0..1] Text 3346
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3346
     ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  3347
       PartyIdentification <PtyId> [1..1] ± 3347
       AccountIdentification <AcctId> [0..1] Text 3347
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3347
     ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  3348
       PartyIdentification <PtyId> [1..1] ± 3348
       AccountIdentification <AcctId> [0..1] Text 3348
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3348
     ReceivingAgentDetails <RcvgAgtDtls> [1..1]  3349
       PartyIdentification <PtyId> [1..1] ± 3349
       AccountIdentification <AcctId> [0..1] Text 3349
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3349
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3340 May 2026
```

