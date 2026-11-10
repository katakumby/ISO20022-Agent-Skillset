---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.2 Account Identification", "7.1.2.2 SecuritiesAccount2Choice", "7.1.2.2.1 Range <Rg>", "7.1.2.2.1.1 From <Fr>"]
file_pages: [249]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.2.2.1.1 From <Fr>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 249 to 249.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 249

```text
Range <Rg> contains the following SecuritiesAccountRange2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   From <Fr> [1..1] ± 249
   To <To> [1..1] ± 249
7.1.2.2.1.1  From <Fr>
Presence: [1..1]
Definition: Securities account number or code at which the range starts.
From <Fr> contains the following elements (see "SecuritiesAccount19" on page 246 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 246
   Type <Tp> [0..1] ± 246
   Name <Nm> [0..1] Text 246
7.1.2.2.1.2  To <To>
Presence: [1..1]
Definition: Securities account number or code at which the range ends.
To <To> contains the following elements (see "SecuritiesAccount19" on page 246 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 246
   Type <Tp> [0..1] ± 246
   Name <Nm> [0..1] Text 246
7.1.2.2.2  Account <Acct>
Presence: [1..*]
Definition: Unique identification of the securities account.
Account <Acct> contains the following elements (see "SecuritiesAccount19" on page 246 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 246
   Type <Tp> [0..1] ± 246
   Name <Nm> [0..1] Text 246
7.1.2.3  AccountIdentification4Choice
Definition: Specifies the unique identification of an account as assigned by the account servicer.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 249 March 2026
```

