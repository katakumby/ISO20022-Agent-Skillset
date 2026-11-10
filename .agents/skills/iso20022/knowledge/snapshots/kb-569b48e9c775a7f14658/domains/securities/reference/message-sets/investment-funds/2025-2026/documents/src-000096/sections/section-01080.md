---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "39.4 Message Building Blocks", "39.4.16 MarketPracticeVersion <MktPrctcVrsn>"]
file_pages: [1488]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.019.001.09"]
---

# 39.4.16 MarketPracticeVersion <MktPrctcVrsn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1488 to 1488.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1488

```text
Definition: Additional information about the product transfer.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
39.4.16 MarketPracticeVersion <MktPrctcVrsn>
Presence: [0..1]
Definition: Identifies the market practice to which the message conforms.
MarketPracticeVersion <MktPrctcVrsn> contains the following elements (see
"MarketPracticeVersion1" on page 4818 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 4818
   Date <Dt> [0..1] YearMonth 4819
   Number <Nb> [0..1] Text 4819
39.4.17 Extension <Xtnsn>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C12 "ExtensionRule"
Extension <Xtnsn> contains the following elements (see "Extension1" on page 4835 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [1..1] Text 4836
   Text <Txt> [1..1] Text 4836
Constraints
• ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1488 May 2026
```

