---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.60 MatchingProcess1Code"]
file_pages: [2087]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.60 MatchingProcess1Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2087 to 2087.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2087

```text
Type: CodeSet
CodeName Name Definition
FUND Fund The place is a fund (transfer agent, fund
itself, etc.).
LMAR LocalMarket The place is a local market.
THEO Theoretical The place is theoretical.
VEND Vendor The place is a vendor.
SCAS SmartContractAutomatedPricingSystem Source of price quotation is a smart
contract automated pricing system.
35.2.2.60  MatchingProcess1Code
Definition: Specifies the action to be performed on the matching process.
Type: CodeSet
CodeName Name Definition
UNMT Unmatch The referenced transaction is requested
to be unmatched.
MTRE ResumeMatching Matching process is to be resumed for
the referenced transaction.
35.2.2.61  MatchingStatus1Code
Definition: Provides the matching status of the instruction at the time the settlement instruction was
sent.
Type: CodeSet
CodeName Name Definition
MACH Matched Instruction has been matched.
NMAT Unmatched Instruction has not been matched.
35.2.2.62  ModifiedStatusReason1Code
Definition: Specifies that the transaction has been modified.
Type: CodeSet
CodeName Name Definition
MDBY ModifiedByYourself Modification of a transaction by the
account owner.
OTHR Other Other. See Narrative.
35.2.2.63  NoReasonCode
Definition: Specifies that there is no reason available.
Type: CodeSet
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2087 March 2026
```

