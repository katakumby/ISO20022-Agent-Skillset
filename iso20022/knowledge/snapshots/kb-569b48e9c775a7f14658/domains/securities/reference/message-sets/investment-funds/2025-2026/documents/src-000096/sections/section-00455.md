---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "28.4 Message Building Blocks", "28.4.6 MasterReference <MstrRef>", "28.4.7.10 FinancialInstrumentDetails <FinInstrmDtls>"]
file_pages: [628]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.005.001.10"]
---

# 28.4.7.10 FinancialInstrumentDetails <FinInstrmDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 628 to 628.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 628

```text
28.4.7.10  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [1..1]
Definition: Information related to the financial instrument to be transferred.
Impacted by: C19 "IdentificationGuideline"
FinancialInstrumentDetails <FinInstrmDtls> contains the following FinancialInstrument116
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  629
{Or     ISIN <ISIN> [1..1] IdentifierSet 629
Or     SEDOL <SEDOL> [1..1] IdentifierSet 630
Or     CUSIP <CUSIP> [1..1] IdentifierSet 630
Or     RIC <RIC> [1..1] IdentifierSet 630
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 630
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 630
Or     CTA <CTA> [1..1] IdentifierSet 630
Or     QUICK <QUICK> [1..1] IdentifierSet 630
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 631
Or     Dutch <Dtch> [1..1] IdentifierSet 631
Or     Valoren <Vlrn> [1..1] IdentifierSet 631
Or     Sicovam <SCVM> [1..1] IdentifierSet 631
Or     Belgian <Belgn> [1..1] IdentifierSet 631
Or     Common <Cmon> [1..1] IdentifierSet 631
Or     DTI <DTI> [1..1] IdentifierSet 631
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  631
       Identification <Id> [1..1] Text 632
       IdentificationSource <IdSrc> [1..1] ± 632
   Name <Nm> [0..1] Text 632
   ShortName <ShrtNm> [0..1] Text 632
   SupplementaryIdentification <SplmtryId> [0..1] Text 632
   ClassType <ClssTp> [0..1] Text 632
   SecuritiesForm <SctiesForm> [0..1] CodeSet 633
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 633
   DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 633
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 628 May 2026
```

