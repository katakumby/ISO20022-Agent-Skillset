---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.5 Balance", "37.1.5.1 CashBalance13", "37.1.5.1.8 RestrictionType <RstrctnTp>", "37.1.5.1.8.2 Description <Desc>"]
file_pages: [799]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.5.1.8.2 Description <Desc>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 799 to 799.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 799

```text
Type <Tp> contains the following elements (see "GenericIdentification1" on page 809 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 809
   SchemeName <SchmeNm> [0..1] Text 809
   Issuer <Issr> [0..1] Text 809
37.1.5.1.8.2  Description <Desc>
Presence: [0..1]
Definition: Description of the restriction.
Datatype: "Max140Text" on page 888
37.1.5.1.8.3  ProcessingType <PrcgTp>
Presence: [0..1]
Definition: Classification of the type of processing restriction that the system should apply for the
restriction.
ProcessingType <PrcgTp> contains one of the following ProcessingType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 799
Or}   Proprietary <Prtry> [1..1] Text 800
37.1.5.1.8.3.1  Code <Cd>
Presence: [1..1]
Definition: Type of processing restrictions, in a coded form.
Datatype: "ProcessingType1Code" on page 871
CodeName Name Definition
RJCT Rejection Restriction is the rejection during the
settlement instruction validation.
CVHD CSDValidationHold Restriction is setting the CSD validation
automatically to hold when accepting a
settlement instruction.
RSVT Reservation Restriction is the creation of a
reservation of a cash balance or a
securities position for a specific purpose.
BLCK Blocking Restriction is the blocking of a party,
securities account, security or cash
account from settlement, blocking of
securities position or cash balance for a
specific purpose.
EARM Earmarking Restriction of linked to the balance type
that defines and manages position types
for securities positions.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 799 February 2025
```

