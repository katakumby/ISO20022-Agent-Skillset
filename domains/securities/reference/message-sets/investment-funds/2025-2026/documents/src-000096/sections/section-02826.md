---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.20 SubscriptionLegDetails <SbcptLegDtls>", "55.4.5.20.18 SettlementAndCustodyDetails <SttlmAndCtdyDtls>"]
file_pages: [3970, 3971]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.20.18 SettlementAndCustodyDetails <SttlmAndCtdyDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3970 to 3971.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3970

```text
Constraints
• TaxElementRule
One of the elements (TaxableIncomePerDividend, EUCapitalGain, EUDividendStatus,
PercentageOfDebtClaim, IndividualTax) must be present.
55.4.5.20.18  SettlementAndCustodyDetails <SttlmAndCtdyDtls>
Presence: [0..1]
Definition: Parameters used to execute the settlement of an investment fund order.
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3970 May 2026
```

## File page 3971

```text
SettlementAndCustodyDetails <SttlmAndCtdyDtls> contains the following
FundSettlementParameters28 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementDate <SttlmDt> [0..1] Date 3972
   SettlementPlace <SttlmPlc> [1..1]  3972
     Party <Pty> [1..1]  3973
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C4 3973
Or       ProprietaryIdentification <PrtryId> [1..1] ± 3973
Or       NameAndAddress <NmAndAdr> [1..1] ± 3974
Or}       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3974
     LEI <LEI> [0..1] IdentifierSet 3974
   SafekeepingPlace <SfkpgPlc> [0..1] ± 3974
   SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 3975
   TradeTransactionCondition <TradTxCond> [0..*] ± 3975
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 3975
   ReceivingSideDetails <RcvgSdDtls> [0..1]  C32,
C33
3976
     ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  3977
       PartyIdentification <PtyId> [1..1] ± 3977
       AccountIdentification <AcctId> [0..1] Text 3977
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3977
     ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  3978
       PartyIdentification <PtyId> [1..1] ± 3978
       AccountIdentification <AcctId> [0..1] Text 3978
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3978
     ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  3979
       PartyIdentification <PtyId> [1..1] ± 3979
       AccountIdentification <AcctId> [0..1] Text 3979
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3979
     ReceivingAgentDetails <RcvgAgtDtls> [1..1]  3980
       PartyIdentification <PtyId> [1..1] ± 3980
       AccountIdentification <AcctId> [0..1] Text 3980
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3980
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3971 May 2026
```

