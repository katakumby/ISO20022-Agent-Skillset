---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.29 Eligibility1Code"]
file_pages: [624]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.29 Eligibility1Code

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 624 to 624.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 624

```text
CodeName Name Definition
APMT AgainstPayment Indicates that the delivery is against
payment.
FREE Free Indicates the delivery is free of payment.
TRIP Triparty Indicates that a custodian bank or
international clearing organization acts
as an intermediary between the two
parties to the repo.
HOIC HoldInCustody Indicates that the collateral pledged by
the (cash) borrower is not actually
delivered to the cash lender. Rather, it is
placed in an internal account ("held in
custody") by the borrower, for the lender,
throughout the duration of the trade.
7.2.2.29  Eligibility1Code
Definition: Identifies the type of investor. The rules that apply to each type of client are different.
Type: CodeSet
CodeName Name Definition
ELIG EligibleCounterparty Eligible customers are the most
sophisticated level of investor, able to
opt out of some the protections afforded
by conduct of business rules.
RETL RetailClient Retail customers are the least
sophisticated level of investor.
PROF ProfessionalClient Professional customers are, for example,
investment firms, credit institutions,
insurance companies.
7.2.2.30  EUCapitalGain2Code
Definition: Specifies whether capital gain is in the scope of the European directive on taxation of
savings income in the form of interest payments (Council Directive 2003/48/EC 3 June) for an income
realised upon sale, a refund or redemption of shares and units etc.
Type: CodeSet
CodeName Name Definition
EUSI CapitalGainInScope Capital gain is in the scope of the
directive.
EUSO CapitalGainOutScope Capital gain is out of the scope of the
directive.
UKWN CapitalGainUnknown Unknown whether capital gain is in or
out of the scope of the directive.
7.2.2.31  EventFrequency3Code
Definition: Specifies the regularity of an event.
Type: CodeSet
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 624 February 2025
```

