---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.6 Indicator"]
file_pages: [3323]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.6 Indicator

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3323 to 3323.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3323

```text
Type: IdentifierSet
Identification scheme: Parties to a trade; UTIIdentier
Format
pattern [A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}
82.2.6 Indicator
82.2.6.1  PaymentDirectionIndicator
Definition: The direction of capital repayment for asset backed securities.
Type: Indicator
Meaning When True: Up
Meaning When False: Down
82.2.6.2  PlusOrMinusIndicator
Definition: Indicates a positive or negative value.
Type: Indicator
Meaning When True: Plus
Meaning When False: Minus
82.2.6.3  RequestedIndicator
Definition: Indicates if requested or not.
Type: Indicator
Meaning When True: Requested
Meaning When False: Not Requested
82.2.6.4  TrueFalseIndicator
Definition: A flag indicating a True or False value.
Type: Indicator
Meaning When True: True
Meaning When False: False
82.2.6.5  YesNoIndicator
Definition: Indicates a "Yes" or "No" type of answer for an element.
Type: Indicator
Meaning When True: Yes
Meaning When False: No
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3323 August 2026
```

