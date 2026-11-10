---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.57 AdditionalBusinessProcessFormat18Choice", "16.1.15.57.2 Proprietary <Prtry>"]
file_pages: [981]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.57.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 981 to 981.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 981

```text
CodeName Name Definition
FPRE FullPrefunding Full pre-funding of a debt instrument by
the issuer prior to original maturity when
the issuer deposits assets in trust.
Applicable only in the frame of a partial
defeasance corporate action event.
REAC RequiredAction Proceeds / entitlements of the
mandatory event can only be paid if
specified action is taken by the account
owner.
INCP IncentivePremiumPayment The event is a payment of an incentive
premium related to the voting conditions
prescribed at a general meeting.
16.1.15.57.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the additional business process "tax refund" linked to a corporate
action event.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.58  UpdateType15Choice
Definition: Choice of format for the update information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 981
Or}   Proprietary <Prtry> [1..1] ± 981
16.1.15.58.1  Code <Cd>
Presence: [1..1]
Definition: Indicates whether the report is complete or contains changes only.
Datatype: "StatementUpdateType1Code" on page 1242
CodeName Name Definition
COMP Complete Statement is complete.
DELT Delta Statement contains changes only.
16.1.15.58.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 981 February 2026
```

