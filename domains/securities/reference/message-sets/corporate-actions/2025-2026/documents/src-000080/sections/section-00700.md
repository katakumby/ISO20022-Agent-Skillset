---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.6 CorporateActionOption40Choice"]
file_pages: [892, 893]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.6 CorporateActionOption40Choice

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 892 to 893.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 892

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.6  CorporateActionOption40Choice
Definition: Choice between a standard code or a proprietary code to specify the type of the corporate
action option.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 892
Or}   Proprietary <Prtry> [1..1] ± 894
16.1.15.6.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the corporate action options available to the account owner.
Datatype: "CorporateActionOption16Code" on page 1200
CodeName Name Definition
ABST Abstain Vote expressed as abstain. In this case,
the issuing company will add the number
of shares to the quorum of the meeting.
If the voting right is not executed, it will
not be added to the quorum. In this case,
code NOAC should be used.
BSPL BonusSharePlan Receive equities from the share
premium reserve of the company and
considered as a capital distribution
rather than a disbursement of income
with different tax implications (typically
found in Australia).
BUYA BuyUp Buy additional securities to round up
position.
CASE CashAndSecurity Option to choose between different
security and cash options.
CASH Cash Option to choose cash.
CERT Certification Certification is provided.
CEXC ConsentAndExchange Vote to consent to change the terms of
the securities agreement and to
exchange securities.
CONN ConsentDenied Vote not to approve the event or
proposal.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 892 February 2026
```

## File page 893

```text
CodeName Name Definition
CONY ConsentGranted Vote to approve the event or proposal.
CTEN ConsentAndTender Vote to consent to change the terms of
the securities agreement and to tender
securities for cash.
EXER Exercise Exercise intermediate securities or
warrants.
LAPS Lapse Allow event or entitled security to expire.
MKDW MarkDown Mark down the global certificate as a
result of a corporate action (instruction
from International Central Securities
Depositories (ICSDs) to common
depositories who are holding the global
certificate on behalf of the International
Central Securities Depositories (ICSDs)).
MKUP MarkUp Mark up the global certificate as a result
of a corporate action (instruction from
International Central Securities
Depositories (ICSDs) to common
depositories who are holding the global
certificate on behalf of the International
Central Securities Depositories (ICSDs)).
MPUT Retain Option that allows a holder to elect to
retain their holding, for example, a
putable bond.
NOAC NoAction Option for the account owner not to take
part in the event. This would include opt-
out for class actions and lodging of
dissenters' rights.
NOQU NonQualifiedInvestor Account owner is a non-qualified
investor.
OFFR ProposedRate In a remarketing of variable notes, the
margin that shareholders can propose in
respect of the next interest period.
OTHR Other Generic corporate action option to be
used in case that no other specific code
is appropriate.
OVER Oversubscribe Subscribe to more equities than
underlying securities position allows.
QINV QualifiedInvestor Account owner is a qualified investor.
SECU Security Distribution of securities to holders.
SLLE SellEntitlement Sell the intermediate securities.
TAXI TaxInstruction Tax instruction.
PRUN UnknownProceeds Proceeds not known during election
period. The option can result in cash
and/or securities.
BOBD BeneficialOwnerBreakdownRequest Breakdown of beneficial ownership
required for withholding tax reclaim
event.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 893 February 2026
```

