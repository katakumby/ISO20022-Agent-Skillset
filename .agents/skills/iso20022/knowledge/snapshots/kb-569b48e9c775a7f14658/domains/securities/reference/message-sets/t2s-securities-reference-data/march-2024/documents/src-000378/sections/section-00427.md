---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.2 Message Datatypes", "13.2.2 CodeSet", "13.2.2.36 PutType1Code"]
file_pages: [522]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.2.2.36 PutType1Code

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 522 to 522.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 522

```text
CodeName Name Definition
VACT VariableCabinetTrade Cabinet trades are used to indicate
prices that trade at a price lower than
that available on an exchange and they
can be fixed or variable (primarily used
for listed futures and options).
13.2.2.36  PutType1Code
Definition: Defines the type of execution of the put feature.
Type: CodeSet
CodeName Name Definition
MAND Mandatory Type of execution of the put feature is
mandatory.
OPTI Optional Type of execution of the put feature is
optional.
TWOS Both Type of execution of the put feature
could be optional or mandatory.
13.2.2.37  RateType12Code
Definition: Specifies the type of rate.
Type: CodeSet
CodeName Name Definition
OPEN Open Rate has not been established.
UKWN Unknown Rate is unknown by the sender or has
not been established.
NILP NilPayment Rate will not be paid.
13.2.2.38  RestrictionType1Code
Definition: Specifies the type of restriction.
Type: CodeSet
CodeName Name Definition
SELR Selling Selling restriction.
BUYR Buying Buying restriction.
PLAR Placing Placing restriction.
HOLR Holding Holding restriction.
VOTR Voting Voting restriction.
13.2.2.39  SecuritiesPaymentStatus1Code
Definition: Specifies the state of payment of a security at a particular time.
Type: CodeSet
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 522 March 2024
```

