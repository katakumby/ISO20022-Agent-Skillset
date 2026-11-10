---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.2 CodeSet", "16.2.2.131 ReturnedStatus1Code"]
file_pages: [1241]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.2.131 ReturnedStatus1Code

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1241 to 1241.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1241

```text
16.2.2.131  ReturnedStatus1Code
Definition: Specifies the reason why the instruction/cancellation request has a returned status.
Type: CodeSet
CodeName Name Definition
NARR NarrativeReason See narrative field for reason.
PROR Prorated Shares returned due to prorated
acceptance.
16.2.2.132  SafekeepingAccountIdentification1Code
Definition: Specifies the account identification via a code.
Type: CodeSet
CodeName Name Definition
GENR General Announcement applies to all
safekeeping accounts that own
underlying financial instrument. (Used for
general or preliminary announcements.).
16.2.2.133  SafekeepingPlace1Code
Definition: Specifies the type of place of safekeeping.
Type: CodeSet
CodeName Name Definition
CUST SharesHeldAtLocalCustodian Financial instruments held at a local
custodian.
ICSD SharesHeldAtICSD Financial instruments held at an
International Central Securities
Depository.
NCSD SharesHeldAtNCSD Financial instruments held at a National
Central Securities Depository.
SHHE SharesHeldElsewhere Used for certain financial instruments, for
example, US mutual funds, where
settlement is internal only, that is, there
is no external movement of securities.
16.2.2.134  SafekeepingPlace2Code
Definition: Specifies the type of place of safekeeping.
Type: CodeSet
CodeName Name Definition
SHHE SharesHeldElsewhere Used for certain financial instruments, for
example, US mutual funds, where
settlement is internal only, that is, there
is no external movement of securities.
ALLP AllPlaces All places of safekeeping where the
financial instrument is held.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1241 February 2026
```

