---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "41.4.4.8.15 TransactionOverhead <TxOvrhd>", "41.4.4.8.15.4 DigitalNetworkFee <DgtlNtwkFee>", "41.4.4.8.15.4.2 Quantity <Qty>", "41.4.4.8.15.4.2.2 ProprietaryQuantity <PrtryQty>", "41.4.4.8.15.4.2.2.1 Quantity <Qty>"]
file_pages: [1770, 1771]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.8.15.4.2.2.1 Quantity <Qty>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1770 to 1771.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1770

```text
ProprietaryQuantity <PrtryQty> contains the following ProprietaryQuantity8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity <Qty> [1..1] Quantity 1770
   QuantityType <QtyTp> [1..1] Text 1770
   Issuer <Issr> [1..1] Text 1770
   SchemeName <SchmeNm> [0..1] Text 1770
41.4.4.8.15.4.2.2.1  Quantity <Qty>
Presence: [1..1]
Definition: Provides the proprietary quantity with a decimal number.
Datatype: "DecimalNumber" on page 5400
41.4.4.8.15.4.2.2.2  QuantityType <QtyTp>
Presence: [1..1]
Definition: Identifies the type of proprietary quantity reported.
Datatype: "Exact4AlphaNumericText" on page 5402
41.4.4.8.15.4.2.2.3  Issuer <Issr>
Presence: [1..1]
Definition: Provides information related to issuer in free format.
Datatype: "Max35Text" on page 5403
41.4.4.8.15.4.2.2.4  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Datatype: "Max35Text" on page 5403
41.4.4.8.15.4.3  DigitalLedgerIdentification <DgtlLdgrId>
Presence: [1..1]
Definition: Place of settlement expressed with a Digital Ledger Identifier. It identifies a digital ledger or
distributed ledger system (for example, blockchain or similar platforms).
Datatype: "DTI2024Identifier" on page 5392
41.4.4.8.16  SettlementAndCustodyDetails <SttlmAndCtdyDtls>
Presence: [0..1]
Definition: Parameters used to execute the settlement of an investment fund order.
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1770 May 2026
```

## File page 1771

```text
SettlementAndCustodyDetails <SttlmAndCtdyDtls> contains the following
FundSettlementParameters22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementDate <SttlmDt> [0..1] Date 1772
   SettlementPlace <SttlmPlc> [1..1]  1772
     Party <Pty> [1..1]  1773
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1773
Or       ProprietaryIdentification <PrtryId> [1..1] ± 1773
Or       NameAndAddress <NmAndAdr> [1..1] ± 1774
Or}       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1774
     LEI <LEI> [0..1] IdentifierSet 1774
   SafekeepingPlace <SfkpgPlc> [0..1] ± 1774
   SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 1775
   TradeTransactionCondition <TradTxCond> [0..*] ± 1775
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1775
   ReceivingSideDetails <RcvgSdDtls> [1..1]  C31,
C32
1776
     ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  1777
       PartyIdentification <PtyId> [1..1] ± 1777
       AccountIdentification <AcctId> [0..1] Text 1777
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1777
     ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  1778
       PartyIdentification <PtyId> [1..1] ± 1778
       AccountIdentification <AcctId> [0..1] Text 1778
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1778
     ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  1779
       PartyIdentification <PtyId> [1..1] ± 1779
       AccountIdentification <AcctId> [0..1] Text 1779
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1779
     ReceivingAgentDetails <RcvgAgtDtls> [1..1]  1780
       PartyIdentification <PtyId> [1..1] ± 1780
       AccountIdentification <AcctId> [0..1] Text 1780
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1780
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1771 May 2026
```

