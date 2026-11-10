---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.52 OptionStyle4Code"]
file_pages: [637]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.52 OptionStyle4Code

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 637 to 637.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 637

```text
CodeName Name Definition
RENO Renouncement The option right is renounced.
EXPI Expiration Option right expires.
7.2.2.52  OptionStyle4Code
Definition: Defines how an option can be exercised.
Type: CodeSet
CodeName Name Definition
AMER American Option can be exercised before or on
expiry date.
EURO European Option that can be exercised on expiry
date only.
BERM Bermudan Option that can be exercised on multiple
discrete dates prior to, or on expiry date.
7.2.2.53  OptionType1Code
Definition: Indicates whether it is a Call option (right to purchase a specific underlying asset) or a Put
option (right to sell a specific underlying asset).
Type: CodeSet
CodeName Name Definition
CALL Call Right to buy a quantity of an asset for an
agreed price at exercise date.
PUTO Put Right to sell a quantity of an asset for an
agreed price at exercise date.
7.2.2.54  OwnershipLegalRestrictions1Code
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
7.2.2.55  PositionEffect2Code
Definition: Indicates whether the resulting position after a trade should be an opening position or closing
position.
Type: CodeSet
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 637 February 2025
```

