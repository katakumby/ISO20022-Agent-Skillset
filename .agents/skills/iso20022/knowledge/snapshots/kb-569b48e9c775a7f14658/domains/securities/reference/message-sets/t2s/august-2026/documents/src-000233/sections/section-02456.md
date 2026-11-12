---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.101 OptionType1Code"]
file_pages: [3267]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.101 OptionType1Code

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3267 to 3267.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3267

```text
82.2.2.101  OptionType1Code
Definition: Indicates whether it is a Call option (right to purchase a specific underlying asset) or a Put
option (right to sell a specific underlying asset).
Type: CodeSet
CodeName Name Definition
CALL Call Right to buy a quantity of an asset for an
agreed price at exercise date.
PUTO Put Right to sell a quantity of an asset for an
agreed price at exercise date.
82.2.2.102  OwnershipLegalRestrictions1Code
Definition: Specifies the regulatory restrictions applicable to a financial instrument.
Type: CodeSet
CodeName Name Definition
A144 USLegal144A Ownership or transfer of an unregistered
security issued, pursuant to US legal
restrictions 144A.
NRST NoRestrictions Ownership or transfer of a security that
is not subject to restrictions.
RSTR Restrictions Ownership or transfer of a security that
is subject to restrictions, and not
pursuant to 144A.
82.2.2.103  PartialSettlement2Code
Definition: Information about partial settlement.
Type: CodeSet
CodeName Name Definition
PAIN PartialSettlement Confirmation is for partial settlement.
Part of the transaction remains
unsettled.
PARC PartiallyConfirmed Confirmation is for partial settlement. No
additional settlement will take place.
82.2.2.104  PenaltyAmountType1Code
Definition: Specifies the type of the penalty amount.
Type: CodeSet
CodeName Name Definition
CASH Cash Penalty is based on the amount of cash
failed to be delivered and the penalty
rate is the discount rate of the relevant
currency.
SECU Securities Penalty is based on the quantity of
securities failed to be delivered and
penalty rate of the securities.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3267 August 2026
```

