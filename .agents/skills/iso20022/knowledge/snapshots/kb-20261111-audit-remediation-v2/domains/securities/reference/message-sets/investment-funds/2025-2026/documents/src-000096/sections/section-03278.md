---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.18 Financial Instrument", "66.1.18.12 FinancialInstrument71", "66.1.18.12.7 DistributionPolicy <DstrbtnPlcy>"]
file_pages: [4515]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.18.12.7 DistributionPolicy <DstrbtnPlcy>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4515 to 4515.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4515

```text
Datatype: "FormOfSecurity1Code" on page 5304
CodeName Name Definition
BEAR Bearer The financial instrument does not specify
any registration of ownership, and is
payable to whomever possesses the
certificate.
REGD Registered Shareholder name of the financial
instrument appears in the corporation/
funds books.
66.1.18.12.7  DistributionPolicy <DstrbtnPlcy>
Presence: [0..1]
Definition: Income policy relating to a class type, that is, if income is paid out or retained in the fund.
Datatype: "DistributionPolicy1Code" on page 5294
CodeName Name Definition
DIST Distribution Income is distributed to the investors in
the fund.
ACCU Accumulation Income is added to the capital of the
fund.
66.1.18.12.8  ProductGroup <PdctGrp>
Presence: [0..1]
Definition: Company specific description of a group of funds.
Datatype: "Max140Text" on page 5402
66.1.18.13  SecurityIdentification19
Definition: Identification of a security.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 4516
   OtherIdentification <OthrId> [0..*]  4516
     Identification <Id> [1..1] Text 4516
     Suffix <Sfx> [0..1] Text 4517
     Type <Tp> [1..1] ± 4517
   Description <Desc> [0..1] Text 4517
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4515 May 2026
```

