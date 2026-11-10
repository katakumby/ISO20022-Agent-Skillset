---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.33 CashSettlementDetails <CshSttlmDtls>", "46.4.5.10.33.1 PaymentInstrument <PmtInstrm>", "46.4.5.10.33.1.5 BlockChainCashWallet <BlckChainCshWllt>", "46.4.5.10.33.1.5.4 DigitalLedgerIdentification <DgtlLdgrId>"]
file_pages: [2458, 2459]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.33.1.5.4 DigitalLedgerIdentification <DgtlLdgrId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2458 to 2459.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2458

```text
46.4.5.10.33.1.5.4  DigitalLedgerIdentification <DgtlLdgrId>
Presence: [1..1]
Definition: Place of safekeeping expressed with a Digital Ledger Identifier. It identifies a digital ledger or
distributed ledger system (for example, blockchain or similar platforms).
Datatype: "DTI2024Identifier" on page 5392
46.4.5.10.34  DigitalAssetSettlement <DgtlAsstSttlm>
Presence: [0..1]
Definition: Total quantity of digital asset to be paid or received in exchange for the securities token.
DigitalAssetSettlement <DgtlAsstSttlm> contains the following DigitalPaymentSettlement3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1]  C14,
C15,
C21,
C22,
C28
2458
     ISIN <ISIN> [0..1] IdentifierSet 2460
     OtherIdentification <OthrId> [0..*]  2460
       Identification <Id> [1..1] Text 2460
       Suffix <Sfx> [0..1] Text 2460
       Type <Tp> [1..1]  2460
{Or         Code <Cd> [1..1] CodeSet 2461
Or}         Proprietary <Prtry> [1..1] Text 2462
     Description <Desc> [0..1] Text 2462
   Quantity <Qty> [1..1]  2463
{Or     Quantity <Qty> [1..1] ± C16 2463
Or}     ProprietaryQuantity <PrtryQty> [1..1]  2463
       Quantity <Qty> [1..1] Quantity 2464
       QuantityType <QtyTp> [1..1] Text 2464
       Issuer <Issr> [1..1] Text 2464
       SchemeName <SchmeNm> [0..1] Text 2464
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2464
46.4.5.10.34.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2458 May 2026
```

## File page 2459

```text
Impacted by: C14 "DescriptionPresenceRule", C15 "DescriptionUsageRule", C21 "ISINGuideline", C22
"ISINPresenceRule", C28 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following SecurityIdentification50
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 2460
   OtherIdentification <OthrId> [0..*]  2460
     Identification <Id> [1..1] Text 2460
     Suffix <Sfx> [0..1] Text 2460
     Type <Tp> [1..1]  2460
{Or       Code <Cd> [1..1] CodeSet 2461
Or}       Proprietary <Prtry> [1..1] Text 2462
   Description <Desc> [0..1] Text 2462
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
• DescriptionUsageRule
Description must be used alone as the last resort.
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2459 May 2026
```

