---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.63 Reversible1Code"]
file_pages: [645]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.63 Reversible1Code

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 645 to 645.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 645

```text
7.2.2.63  Reversible1Code
Definition: Indicates the possibility to terminate the securitiesc lending contract either by the borrower or
lender before the expiration date.
Type: CodeSet
CodeName Name Definition
REVL Reversible Securities lending contract can be ended
by the borrower before the expiration
date.
FIXD Fixed Securities lending contract can not be
ended by the borrower before the
expiration date.
CABK CallBack Securities lending contract can be ended
by the lender before the expiration date.
7.2.2.64  SecuritiesAccountPurposeType1Code
Definition: Specifies the purpose of the securities account.
Type: CodeSet
CodeName Name Definition
MARG Margin Account is used when financing is done
by the broker.
SHOR ShortSale Account is used for short sale orders.
ABRD Abroad Account is located in a financial
institution outside the country where the
transaction is taking place.
CEND Centralised Account and all its related positions are
held in one location.
DVPA CashDVP Account is used for settlement upon
delivery, or a collection on a delivery
basis.
PHYS Physical Account is used for physical domestic
safekeeping.
7.2.2.65  SecuritiesLendingType1Code
Definition: Type of securities lending contract.
Type: CodeSet
CodeName Name Definition
NWRG NewRegistration Securities lending contract is new and
registered.
RENW RollOverRenewal Securities lending contract is renewed.
CABK CallBack Securities lending contract is called
back.
7.2.2.66  SettlementDate5Code
Definition: Specifies the date of settlement, in coded form.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 645 February 2025
```

