---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.19 RedemptionLegDetails <RedLegDtls>", "55.4.5.19.20 SettlementAndCustodyDetails <SttlmAndCtdyDtls>"]
file_pages: [3898, 3899]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.19.20 SettlementAndCustodyDetails <SttlmAndCtdyDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3898 to 3899.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3898

```text
Constraints
• TaxElementRule
One of the elements (TaxableIncomePerDividend, EUCapitalGain, EUDividendStatus,
PercentageOfDebtClaim, IndividualTax) must be present.
55.4.5.19.20  SettlementAndCustodyDetails <SttlmAndCtdyDtls>
Presence: [0..1]
Definition: Parameters used to execute the settlement of an investment fund order.
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3898 May 2026
```

## File page 3899

```text
SettlementAndCustodyDetails <SttlmAndCtdyDtls> contains the following
FundSettlementParameters22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementDate <SttlmDt> [0..1] Date 3900
   SettlementPlace <SttlmPlc> [1..1]  3900
     Party <Pty> [1..1]  3901
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C4 3901
Or       ProprietaryIdentification <PrtryId> [1..1] ± 3901
Or       NameAndAddress <NmAndAdr> [1..1] ± 3902
Or}       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3902
     LEI <LEI> [0..1] IdentifierSet 3902
   SafekeepingPlace <SfkpgPlc> [0..1] ± 3902
   SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 3903
   TradeTransactionCondition <TradTxCond> [0..*] ± 3903
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 3903
   ReceivingSideDetails <RcvgSdDtls> [1..1]  C32,
C33
3904
     ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  3905
       PartyIdentification <PtyId> [1..1] ± 3905
       AccountIdentification <AcctId> [0..1] Text 3905
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3905
     ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  3906
       PartyIdentification <PtyId> [1..1] ± 3906
       AccountIdentification <AcctId> [0..1] Text 3906
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3906
     ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  3907
       PartyIdentification <PtyId> [1..1] ± 3907
       AccountIdentification <AcctId> [0..1] Text 3907
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3907
     ReceivingAgentDetails <RcvgAgtDtls> [1..1]  3908
       PartyIdentification <PtyId> [1..1] ± 3908
       AccountIdentification <AcctId> [0..1] Text 3908
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3908
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3899 May 2026
```

