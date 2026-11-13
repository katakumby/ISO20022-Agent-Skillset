---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.21 Quantity", "35.1.21.16 QuantityAndAccount118"]
file_pages: [1742]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.21.16 QuantityAndAccount118

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1742 to 1742.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1742

```text
Following Must be True
    /SafekeepingPlaceFormat Must be present
 Or    /LEI Must be present
35.1.21.16  QuantityAndAccount118
Definition: Details on a quantity, account and other related information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DenominationChoice <DnmtnChc> [0..1] Text 1742
   AccountOwner <AcctOwnr> [0..1] ± 1743
   CashAccount <CshAcct> [0..1] ± 1743
   SafekeepingPlace <SfkpgPlc> [0..1] ± C33 1743
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 1744
Constraints
• DenominationRule
Unless bilaterally agreed between the account owner and servicer, if DenominationChoice is used, it
must not contain information that can be provided in a structured field.
• SafekeepingPlaceGuideline
When used (see usage rule SafekeepingPlaceRule), unless special arrangements exist between the
account servicer and the account owner, it is recommended to use the place of safekeeping field
following the market practice described below:
• SafekeepingPlaceType/SharesHeldAtNCSD: a NCSD's BIC will be used for domestic and NCSD to
NCSD settlement instructions.
• SafekeepingPlaceType/SharesHeldAtICSD: an ICSD's BIC will be used for ICSD internal, ICSD/
local and ICSD to ICSD settlement instructions.
• SafekeepingPlaceType/SharesHeldAtLoaclCustodian: applicable, for instance, when the account
servicer is a global custodian and provides the account owner with a position reporting at global
custodian's agents' level. When instructing, the fund manager would therefore mention, as a place of
safekeeping, the BIC of the global custodian's agent on the market.
Absence of SafekeepingPlace means that:
• The SafekeepingPlace information is kept by the account servicer (SLA, account structure, ETC.)
and should not be provided by the account owner.
• The SafekeepingPlace is the counterparty's Depository. The transaction is therefore domestic (to
an NCSD) or internal to an ICSD.
For more details, see the relevant market practice document on www.smpg.info.
35.1.21.16.1  DenominationChoice <DnmtnChc>
Presence: [0..1]
Definition: Denomination of the security to be received or delivered.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1742 March 2026
```

