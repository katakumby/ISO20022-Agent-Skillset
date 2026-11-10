---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.28 SettlementAndCustodyDetails <SttlmAndCtdyDtls>"]
file_pages: [2396, 2397]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.28 SettlementAndCustodyDetails <SttlmAndCtdyDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2396 to 2397.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2396

```text
Constraints
• TaxElementRule
One of the elements (TaxableIncomePerDividend, EUCapitalGain, EUDividendStatus,
PercentageOfDebtClaim, IndividualTax) must be present.
46.4.5.10.28  SettlementAndCustodyDetails <SttlmAndCtdyDtls>
Presence: [0..1]
Definition: Parameters used to execute the settlement of an investment fund order.
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2396 May 2026
```

## File page 2397

```text
SettlementAndCustodyDetails <SttlmAndCtdyDtls> contains the following
FundSettlementParameters22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementDate <SttlmDt> [0..1] Date 2398
   SettlementPlace <SttlmPlc> [1..1]  2398
     Party <Pty> [1..1]  2399
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C5 2399
Or       ProprietaryIdentification <PrtryId> [1..1] ± 2399
Or       NameAndAddress <NmAndAdr> [1..1] ± 2400
Or}       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2400
     LEI <LEI> [0..1] IdentifierSet 2400
   SafekeepingPlace <SfkpgPlc> [0..1] ± 2400
   SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 2401
   TradeTransactionCondition <TradTxCond> [0..*] ± 2401
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 2401
   ReceivingSideDetails <RcvgSdDtls> [1..1]  C33,
C34
2402
     ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  2403
       PartyIdentification <PtyId> [1..1] ± 2403
       AccountIdentification <AcctId> [0..1] Text 2403
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2403
     ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  2404
       PartyIdentification <PtyId> [1..1] ± 2404
       AccountIdentification <AcctId> [0..1] Text 2404
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2404
     ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  2405
       PartyIdentification <PtyId> [1..1] ± 2405
       AccountIdentification <AcctId> [0..1] Text 2405
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2405
     ReceivingAgentDetails <RcvgAgtDtls> [1..1]  2406
       PartyIdentification <PtyId> [1..1] ± 2406
       AccountIdentification <AcctId> [0..1] Text 2406
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2406
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2397 May 2026
```

