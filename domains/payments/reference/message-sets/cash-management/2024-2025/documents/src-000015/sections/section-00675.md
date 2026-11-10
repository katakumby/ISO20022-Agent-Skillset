---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.2 Message Datatypes", "37.2.2 CodeSet", "37.2.2.11 ErrorHandling1Code"]
file_pages: [852]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.2.2.11 ErrorHandling1Code

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 852 to 852.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 852

```text
CodeName Name Definition
PDNG Pending Booking on the account owner's account
in the account servicer's ledger has not
been completed.
Usage: this can be used for expected
items, or for items for which some
conditions still need to be fulfilled before
they can be booked. If booking takes
place, the entry will be included with
status Booked in subsequent account
report or statement. Status Pending
cannot be reversed.
FUTR Future Entry is on the books of the account
servicer and value will be applied to the
account owner at a future date and time.
37.2.2.11  ErrorHandling1Code
Definition: Error codes generated when the response to a query exceeds the maximum size or the data
is not available.
Type: CodeSet
CodeName Name Definition
X020 DataNotYetAvailable Specifies the error code when the data
requested are not yet available.
X030 MessageSizeLimitExceeded Specifies the error code when the data
requested generates a message size
that exceed the processing capacity.
X050 DataNotAvailable Specifies the error code when the data
requested have not been found.
37.2.2.12  ExternalAccountIdentification1Code
Definition: Specifies the external account identification scheme name code in the format of character
string with a maximum length of 4 characters.
The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
Type: CodeSet
Format
minLength 1
maxLength 4
37.2.2.13  ExternalCancellationReason1Code
Definition: Specifies the cancellation reason, as published in an external cancellation reason code set.
External code sets can be downloaded from www.iso20022.org.
Type: CodeSet
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 852 February 2025
```

