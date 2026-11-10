---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["3 acmt.002.001.08 AccountDetailsConfirmationV08", "3.4 Message Building Blocks"]
file_pages: [43]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.002.001.08"]
---

# 3.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 43 to 43.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 43

```text
C29 PoliticallyExposedPersonTypeRule
If PoliticallyExposedPersonType/Code is 'NoPoliticalExposure' (NPEX) then
PoliticallyExposedPersonStatus is not allowed.
C30 ReferredPlacementAgentRule
ReferredPlacementAgent may only be present if Referred is REFR (Referred).
C31 ReinvestmentPercentage1Rule
Sum of all occurrences of ReinvestmentDetails/ReinvestmentPercentage must not be greater
than 100.
C32 StatusElementRule
One of the elements (Enabled, Disabled, Pending, PendingOpening, Proforma, Closed,
ClosurePending, Other) must be present.
C33 UnitRule
If SavingsInvestmentPlan is present, then SavingsInvestmentPlan/Quantity/Unit is not allowed.
On Condition
    /SavingsInvestmentPlan[*] is present
Following Must be True
    /SavingsInvestmentPlan[*]/Quantity/Unit Must be absent
This constraint is defined at the MessageDefinition level.
C34 ValidationByTable
Must be a valid terrestrial language.
C35 ValidationByTable
Must be a valid nationality.
3.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
3.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
3.4.2 OrderReference <OrdrRef>
Presence: [0..1]
Definition: Identifies a related order or settlement transaction.
Approved by the Securities SEG on 27 January 2026 acmt.002.001.08 AccountDetailsConfirmationV08
Investment Funds - Maintenance 2025 - 2026 43 May 2026
```

