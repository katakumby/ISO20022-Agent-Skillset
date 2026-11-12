---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.2 Account Identification", "82.1.2.3 SecuritiesAccount2Choice", "82.1.2.3.1 Range <Rg>", "82.1.2.3.1.1 From <Fr>"]
file_pages: [2836]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.2.3.1.1 From <Fr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2836 to 2836.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2836

```text
Range <Rg> contains the following SecuritiesAccountRange2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   From <Fr> [1..1] ± 2836
   To <To> [1..1] ± 2836
82.1.2.3.1.1  From <Fr>
Presence: [1..1]
Definition: Securities account number or code at which the range starts.
From <Fr> contains the following elements (see "SecuritiesAccount19" on page 2834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2834
   Type <Tp> [0..1] ± 2834
   Name <Nm> [0..1] Text 2834
82.1.2.3.1.2  To <To>
Presence: [1..1]
Definition: Securities account number or code at which the range ends.
To <To> contains the following elements (see "SecuritiesAccount19" on page 2834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2834
   Type <Tp> [0..1] ± 2834
   Name <Nm> [0..1] Text 2834
82.1.2.3.2  Account <Acct>
Presence: [1..*]
Definition: Unique identification of the securities account.
Account <Acct> contains the following elements (see "SecuritiesAccount19" on page 2834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2834
   Type <Tp> [0..1] ± 2834
   Name <Nm> [0..1] Text 2834
82.1.2.4  AccountIdentification4Choice
Definition: Specifies the unique identification of an account as assigned by the account servicer.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2836 August 2026
```

