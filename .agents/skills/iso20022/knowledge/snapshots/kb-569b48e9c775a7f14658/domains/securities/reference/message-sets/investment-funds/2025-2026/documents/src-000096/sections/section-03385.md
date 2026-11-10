---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.9 InvestmentAccount73", "66.1.24.9.27 Pledging <Pldgg>"]
file_pages: [4629]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.9.27 Pledging <Pldgg>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4629 to 4629.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4629

```text
Definition: Category of the account.
InvestmentAccountCategory <InvstmtAcctCtgy> contains one of the following elements (see
"InvestmentAccountCategory1Choice" on page 4595 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4595
Or}   Proprietary <Prtry> [1..1] ± 4595
66.1.24.9.27  Pledging <Pldgg>
Presence: [0..1]
Definition: Specifies whether the holdings in the account are eligible for pledging.
Datatype: "Eligible1Code" on page 5295
CodeName Name Definition
ELIG Eligible Item is eligible.
NELI NotEligible Item is not eligible.
66.1.24.9.28  Collateral <Coll>
Presence: [0..1]
Definition: Specifies whether the holdings in the account are used as collateral.
Datatype: "Collateral1Code" on page 5285
CodeName Name Definition
COLL Collateral Item is used as collateral.
NCOL NotCollateral Item is not used as collateral.
66.1.24.9.29  ThirdPartyRights <ThrdPtyRghts>
Presence: [0..1]
Definition: Details of third party rights.
ThirdPartyRights <ThrdPtyRghts> contains the following elements (see "ThirdPartyRights2" on
page 4596 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] Text 4596
   DateTime <DtTm> [0..1] DateTime 4596
   Holder <Hldr> [0..1] ± 4596
   LegalEntityIdentifier <LglNttyIdr> [0..1] IdentifierSet 4597
   Amount <Amt> [0..1] Amount C1, C13 4597
   Description <Desc> [0..1] Text 4597
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4629 May 2026
```

