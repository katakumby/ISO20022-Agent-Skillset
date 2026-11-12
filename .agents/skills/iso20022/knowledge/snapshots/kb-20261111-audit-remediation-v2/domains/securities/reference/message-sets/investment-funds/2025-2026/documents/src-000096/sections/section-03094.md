---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03", "65.4 Message Building Blocks", "65.4.2 RequestDetails <ReqDtls>", "65.4.2.3 OrderReference <OrdrRef>", "65.4.2.3.8 FinancialInstrumentDetails <FinInstrmDtls>", "65.4.2.3.8.1 Identification <Id>"]
file_pages: [4317]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.058.001.03"]
---

# 65.4.2.3.8.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4317 to 4317.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4317

```text
Constraints
• IdentificationGuideline
It is recommended that ISIN is used in Identification.
When an ISIN code exists, it is strongly recommended that the ISIN be used.
65.4.2.3.8.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the security by an ISIN.
Identification <Id> contains one of the following SecurityIdentification46Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISIN <ISIN> [1..1] IdentifierSet 4317
Or   SEDOL <SEDOL> [1..1] IdentifierSet 4318
Or   CUSIP <CUSIP> [1..1] IdentifierSet 4318
Or   RIC <RIC> [1..1] IdentifierSet 4318
Or   TickerSymbol <TckrSymb> [1..1] IdentifierSet 4318
Or   Bloomberg <Blmbrg> [1..1] IdentifierSet 4318
Or   CTA <CTA> [1..1] IdentifierSet 4318
Or   QUICK <QUICK> [1..1] IdentifierSet 4318
Or   Wertpapier <Wrtppr> [1..1] IdentifierSet 4319
Or   Dutch <Dtch> [1..1] IdentifierSet 4319
Or   Valoren <Vlrn> [1..1] IdentifierSet 4319
Or   Sicovam <SCVM> [1..1] IdentifierSet 4319
Or   Belgian <Belgn> [1..1] IdentifierSet 4319
Or   Common <Cmon> [1..1] IdentifierSet 4319
Or   DTI <DTI> [1..1] IdentifierSet 4319
Or}   OtherProprietaryIdentification <OthrPrtryId> [1..1]  4319
     Identification <Id> [1..1] Text 4320
     IdentificationSource <IdSrc> [1..1] ± 4320
65.4.2.3.8.1.1  ISIN <ISIN>
Presence: [1..1]
Definition: International Securities Identification Number (ISIN). A numbering system designed by the
United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-
character prefix representing the country of issue, followed by the national security number (if one
exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for
securities in that country.
Approved by the Securities SEG on 27 January 2026 setr.058.001.03
RequestForOrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4317 May 2026
```

