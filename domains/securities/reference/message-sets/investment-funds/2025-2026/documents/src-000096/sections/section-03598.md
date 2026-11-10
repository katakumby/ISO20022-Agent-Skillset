---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.23 InvestorProfile2", "66.1.28.23.1 Type <Tp>", "66.1.28.23.1.1 Code <Cd>"]
file_pages: [4848]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.23.1.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4848 to 4848.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4848

```text
Type <Tp> contains one of the following ProfileType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4848
Or}   Proprietary <Prtry> [1..1] ± 4848
66.1.28.23.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of profile expressed as a code.
Datatype: "ProfileType1Code" on page 5345
CodeName Name Definition
HEDG Hedge Investor shares that uses defensive
operations (hedging), thus avoiding the
risk of large swings.
HFTR HighFrequencyTrader Investors operating through algorithms
and send orders automatically according
to the strategies defined by their
managers. Through this access model,
the participants of these servers are
hosted primarily within the premises of
Brazilian Market and significantly reduce
the time of submission of offers to
trading systems.
MAKE MarketMaker Agent liquidity, liquidity facilitator,
promoter of business, specialist, market
maker and liquidity provider are some
designations given to those who propose
to provide liquidity and minimum
reference price for assets previously
accredited, factors highlighted in the
analysis of efficiency in capital markets.
TREA Treasury Trading system of federal securities in
the retail market directly to the investor.
The operation can be performed directly
over the Internet.
66.1.28.23.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of profile expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4848 May 2026
```

