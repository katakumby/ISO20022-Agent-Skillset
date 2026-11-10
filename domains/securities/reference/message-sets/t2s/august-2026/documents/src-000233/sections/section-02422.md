---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.6 AddressType1Code"]
file_pages: [3213]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.6 AddressType1Code

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3213 to 3213.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3213

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
82.2.2.6  AddressType1Code
Definition: Specifies the type of address.
Type: CodeSet
CodeName Name Definition
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
82.2.2.7  AddressType2Code
Definition: Specifies the type of address.
Type: CodeSet
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
MLTO MailTo Address is the address to which mail is
sent.
DLVY DeliveryTo Address is the address to which delivery
is to take place.
82.2.2.8  AdjustmentDirection1Code
Definition: Specifies whether the adjustment is added or subtracted to the total amount.
Type: CodeSet
CodeName Name Definition
ADDD Added Adjustment amount must be added to
the total amount.
SUBS Substracted Adjustment amount must be substracted
from the total amount.
82.2.2.9  Appearance1Code
Definition: Specifies the deliverability of a security.
Type: CodeSet
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3213 August 2026
```

