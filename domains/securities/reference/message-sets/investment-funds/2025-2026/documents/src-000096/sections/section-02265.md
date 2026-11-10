---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.22 CashSettlementDetails <CshSttlmDtls>", "50.4.4.9.22.1 PaymentInstrument <PmtInstrm>", "50.4.4.9.22.1.7 BlockChainCashWallet <BlckChainCshWllt>", "50.4.4.9.22.1.7.4 DigitalLedgerIdentification <DgtlLdgrId>"]
file_pages: [3171, 3172]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.22.1.7.4 DigitalLedgerIdentification <DgtlLdgrId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3171 to 3172.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3171

```text
50.4.4.9.22.1.7.4  DigitalLedgerIdentification <DgtlLdgrId>
Presence: [1..1]
Definition: Place of safekeeping expressed with a Digital Ledger Identifier. It identifies a digital ledger or
distributed ledger system (for example, blockchain or similar platforms).
Datatype: "DTI2024Identifier" on page 5392
50.4.4.9.23  DigitalAssetSettlement <DgtlAsstSttlm>
Presence: [0..1]
Definition: Total quantity of digital asset to be paid or received in exchange for the securities token.
DigitalAssetSettlement <DgtlAsstSttlm> contains the following DigitalPaymentSettlement3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1]  C13,
C14,
C22,
C23,
C27
3171
     ISIN <ISIN> [0..1] IdentifierSet 3173
     OtherIdentification <OthrId> [0..*]  3173
       Identification <Id> [1..1] Text 3173
       Suffix <Sfx> [0..1] Text 3173
       Type <Tp> [1..1]  3173
{Or         Code <Cd> [1..1] CodeSet 3174
Or}         Proprietary <Prtry> [1..1] Text 3175
     Description <Desc> [0..1] Text 3175
   Quantity <Qty> [1..1]  3176
{Or     Quantity <Qty> [1..1] ± C15 3176
Or}     ProprietaryQuantity <PrtryQty> [1..1]  3176
       Quantity <Qty> [1..1] Quantity 3177
       QuantityType <QtyTp> [1..1] Text 3177
       Issuer <Issr> [1..1] Text 3177
       SchemeName <SchmeNm> [0..1] Text 3177
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3177
50.4.4.9.23.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3171 May 2026
```

## File page 3172

```text
Impacted by: C13 "DescriptionPresenceRule", C14 "DescriptionUsageRule", C22 "ISINGuideline", C23
"ISINPresenceRule", C27 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following SecurityIdentification50
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 3173
   OtherIdentification <OthrId> [0..*]  3173
     Identification <Id> [1..1] Text 3173
     Suffix <Sfx> [0..1] Text 3173
     Type <Tp> [1..1]  3173
{Or       Code <Cd> [1..1] CodeSet 3174
Or}       Proprietary <Prtry> [1..1] Text 3175
   Description <Desc> [0..1] Text 3175
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
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3172 May 2026
```

