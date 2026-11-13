---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.28 SettlementAndCustodyDetails <SttlmAndCtdyDtls>"]
file_pages: [2854, 2855]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.28 SettlementAndCustodyDetails <SttlmAndCtdyDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2854 to 2855.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2854

```text
Constraints
• TaxElementRule
One of the elements (TaxableIncomePerDividend, EUCapitalGain, EUDividendStatus,
PercentageOfDebtClaim, IndividualTax) must be present.
49.4.5.9.28  SettlementAndCustodyDetails <SttlmAndCtdyDtls>
Presence: [0..1]
Definition: Parameters used to execute the settlement of an investment fund order.
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2854 May 2026
```

## File page 2855

```text
SettlementAndCustodyDetails <SttlmAndCtdyDtls> contains the following
FundSettlementParameters28 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementDate <SttlmDt> [0..1] Date 2856
   SettlementPlace <SttlmPlc> [1..1]  2856
     Party <Pty> [1..1]  2857
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C5 2857
Or       ProprietaryIdentification <PrtryId> [1..1] ± 2857
Or       NameAndAddress <NmAndAdr> [1..1] ± 2858
Or}       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2858
     LEI <LEI> [0..1] IdentifierSet 2858
   SafekeepingPlace <SfkpgPlc> [0..1] ± 2858
   SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 2859
   TradeTransactionCondition <TradTxCond> [0..*] ± 2859
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 2859
   ReceivingSideDetails <RcvgSdDtls> [0..1]  C33,
C34
2860
     ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  2861
       PartyIdentification <PtyId> [1..1] ± 2861
       AccountIdentification <AcctId> [0..1] Text 2861
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2861
     ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  2862
       PartyIdentification <PtyId> [1..1] ± 2862
       AccountIdentification <AcctId> [0..1] Text 2862
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2862
     ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  2863
       PartyIdentification <PtyId> [1..1] ± 2863
       AccountIdentification <AcctId> [0..1] Text 2863
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2863
     ReceivingAgentDetails <RcvgAgtDtls> [1..1]  2864
       PartyIdentification <PtyId> [1..1] ± 2864
       AccountIdentification <AcctId> [0..1] Text 2864
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2864
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2855 May 2026
```

