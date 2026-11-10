---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.16 RedemptionLegDetails <RedLegDtls>", "53.4.5.16.9 TransactionOverhead <TxOvrhd>", "53.4.5.16.9.4 DigitalNetworkFee <DgtlNtwkFee>", "53.4.5.16.9.4.2 Quantity <Qty>", "53.4.5.16.9.4.2.2 ProprietaryQuantity <PrtryQty>", "53.4.5.16.9.4.2.2.1 Quantity <Qty>"]
file_pages: [3589, 3590]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.16.9.4.2.2.1 Quantity <Qty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3589 to 3590.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3589

```text
ProprietaryQuantity <PrtryQty> contains the following ProprietaryQuantity8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity <Qty> [1..1] Quantity 3589
   QuantityType <QtyTp> [1..1] Text 3589
   Issuer <Issr> [1..1] Text 3589
   SchemeName <SchmeNm> [0..1] Text 3589
53.4.5.16.9.4.2.2.1  Quantity <Qty>
Presence: [1..1]
Definition: Provides the proprietary quantity with a decimal number.
Datatype: "DecimalNumber" on page 5400
53.4.5.16.9.4.2.2.2  QuantityType <QtyTp>
Presence: [1..1]
Definition: Identifies the type of proprietary quantity reported.
Datatype: "Exact4AlphaNumericText" on page 5402
53.4.5.16.9.4.2.2.3  Issuer <Issr>
Presence: [1..1]
Definition: Provides information related to issuer in free format.
Datatype: "Max35Text" on page 5403
53.4.5.16.9.4.2.2.4  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Datatype: "Max35Text" on page 5403
53.4.5.16.9.4.3  DigitalLedgerIdentification <DgtlLdgrId>
Presence: [1..1]
Definition: Place of settlement expressed with a Digital Ledger Identifier. It identifies a digital ledger or
distributed ledger system (for example, blockchain or similar platforms).
Datatype: "DTI2024Identifier" on page 5392
53.4.5.16.10  SettlementAndCustodyDetails <SttlmAndCtdyDtls>
Presence: [0..1]
Definition: Parameters used to execute the settlement of an investment fund order.
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3589 May 2026
```

## File page 3590

```text
SettlementAndCustodyDetails <SttlmAndCtdyDtls> contains the following
FundSettlementParameters28 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementDate <SttlmDt> [0..1] Date 3591
   SettlementPlace <SttlmPlc> [1..1]  3591
     Party <Pty> [1..1]  3592
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C4 3592
Or       ProprietaryIdentification <PrtryId> [1..1] ± 3592
Or       NameAndAddress <NmAndAdr> [1..1] ± 3593
Or}       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3593
     LEI <LEI> [0..1] IdentifierSet 3593
   SafekeepingPlace <SfkpgPlc> [0..1] ± 3593
   SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 3594
   TradeTransactionCondition <TradTxCond> [0..*] ± 3594
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 3594
   ReceivingSideDetails <RcvgSdDtls> [0..1]  C33,
C34
3595
     ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  3596
       PartyIdentification <PtyId> [1..1] ± 3596
       AccountIdentification <AcctId> [0..1] Text 3596
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3596
     ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  3597
       PartyIdentification <PtyId> [1..1] ± 3597
       AccountIdentification <AcctId> [0..1] Text 3597
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3597
     ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  3598
       PartyIdentification <PtyId> [1..1] ± 3598
       AccountIdentification <AcctId> [0..1] Text 3598
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3598
     ReceivingAgentDetails <RcvgAgtDtls> [1..1]  3599
       PartyIdentification <PtyId> [1..1] ± 3599
       AccountIdentification <AcctId> [0..1] Text 3599
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3599
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3590 May 2026
```

