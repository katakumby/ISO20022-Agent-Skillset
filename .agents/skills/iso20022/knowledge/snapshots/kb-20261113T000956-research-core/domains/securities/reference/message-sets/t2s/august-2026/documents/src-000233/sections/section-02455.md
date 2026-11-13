---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.98 OptionParty1Code"]
file_pages: [3266]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.98 OptionParty1Code

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3266 to 3266.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3266

```text
CodeName Name Definition
SMEQ SmallerOrEqualTo Smaller or equal to.
GREA GreaterThan Greater than.
GREQ GreaterOrEqualTo Greater or equal to.
EQAL EqualTo Equal to.
82.2.2.98  OptionParty1Code
Definition: Specifies if a trade party is a buyer or a seller.
Type: CodeSet
CodeName Name Definition
SLLR Seller Seller in a trade.
BYER Buyer Buyer in a trade.
82.2.2.99  OptionStyle1Code
Definition: Defines how an option can be exercised.
Type: CodeSet
CodeName Name Definition
AMER American Option can be exercised before or on
expiry date.
EURO European Option that can be exercised on expiry
date only.
BERM Bermudan Option that can be exercised on multiple
discrete dates prior to, or on expiry date.
ASIA Asian Option where the payoff is not
determined by the underlying price at
maturity but by the average underlying
price over some pre-set period of time.
CANA Canary Option whose exercise style lies
somewhere between European options
and Bermudan options. The holder can
exercise the option at quarterly dates,
but not before a set time period (typically
one year) has elapsed.
82.2.2.100  OptionStyle2Code
Definition: Defines how an option can be exercised.
Type: CodeSet
CodeName Name Definition
AMER American Option can be exercised before or on
expiry date.
EURO European Option that can be exercised on expiry
date only.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3266 August 2026
```

