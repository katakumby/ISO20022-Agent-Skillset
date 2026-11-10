---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.17 Conversion <Convs>", "34.4.4.17.1 SourceSecurity <SrcScty>", "34.4.4.17.1.1 Identification <Id>"]
file_pages: [887]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.17.1.1 Identification <Id>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 887 to 887.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 887

```text
Constraints
• IdentificationGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
34.4.4.17.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier of a security, assigned under a formal or proprietary
identification scheme.
Identification <Id> contains one of the following SecurityIdentification46Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISIN <ISIN> [1..1] IdentifierSet 887
Or   SEDOL <SEDOL> [1..1] IdentifierSet 888
Or   CUSIP <CUSIP> [1..1] IdentifierSet 888
Or   RIC <RIC> [1..1] IdentifierSet 888
Or   TickerSymbol <TckrSymb> [1..1] IdentifierSet 888
Or   Bloomberg <Blmbrg> [1..1] IdentifierSet 888
Or   CTA <CTA> [1..1] IdentifierSet 888
Or   QUICK <QUICK> [1..1] IdentifierSet 888
Or   Wertpapier <Wrtppr> [1..1] IdentifierSet 889
Or   Dutch <Dtch> [1..1] IdentifierSet 889
Or   Valoren <Vlrn> [1..1] IdentifierSet 889
Or   Sicovam <SCVM> [1..1] IdentifierSet 889
Or   Belgian <Belgn> [1..1] IdentifierSet 889
Or   Common <Cmon> [1..1] IdentifierSet 889
Or   DTI <DTI> [1..1] IdentifierSet 889
Or}   OtherProprietaryIdentification <OthrPrtryId> [1..1]  889
     Identification <Id> [1..1] Text 890
     IdentificationSource <IdSrc> [1..1] ± 890
34.4.4.17.1.1.1  ISIN <ISIN>
Presence: [1..1]
Definition: International Securities Identification Number (ISIN). A numbering system designed by the
United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-
character prefix representing the country of issue, followed by the national security number (if one
exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for
securities in that country.
Datatype: "ISINOct2015Identifier" on page 5395
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 887 May 2026
```

