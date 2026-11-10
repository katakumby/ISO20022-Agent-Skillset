---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.160 ShortLong1Code"]
file_pages: [3304]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.160 ShortLong1Code

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3304 to 3304.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3304

```text
CodeName Name Definition
SAGE SettlingAgent Settlement party is trading and settling
transactions in financial instruments on
behalf of its client(s).
CUST SettlingCustodian Settlement party is a custodian. It
receives/delivers the securities and
carries out custodial duties.
SPRI SettlingPrincipal Settlement party is settling its own
trades.
RISP SettlingRisklessPrincipal Party settles trades that were
simultaneously offset.
82.2.2.160  ShortLong1Code
Definition: Specifies whether the securities position is short or long, that is, whether the balance is a
negative or positive balance.
Type: CodeSet
CodeName Name Definition
SHOR Short Position is short, that is, the balance is
negative.
LONG Long Position is long, that is, the balance is
positive.
82.2.2.161  Standardisation1Code
Definition: Specifies whether the terms of the security (underlying instruments, expiration date, contract
size) are defined according to the exchange specifications or whether they can be user defined.
Type: CodeSet
CodeName Name Definition
FLEX Flexible Derivatives defined according to
exchange specifications, but certain
characteristics can be user defined.
NSTA NonStandardised Custom-made instrument between two
parties. Underlying
instruments, expiration date and contract
size of the derivatives are not
standardised.
STAN Standardised The underlying instruments, expiration
date and contract size of the derivatives
are standardised.
82.2.2.162  StatementUpdateType1Code
Definition: Specifies the nature of a statement update, for example, it is a complete statement.
Type: CodeSet
CodeName Name Definition
COMP Complete Statement is complete.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3304 August 2026
```

