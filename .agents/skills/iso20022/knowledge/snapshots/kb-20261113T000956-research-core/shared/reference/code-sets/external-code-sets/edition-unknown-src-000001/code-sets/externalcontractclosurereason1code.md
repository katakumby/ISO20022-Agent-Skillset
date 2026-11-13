---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalContractClosureReason1Code"]
code_set: "ExternalContractClosureReason1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalContractClosureReason1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalContractClosureReason1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies a contract closure reason code, as published in the external ISO 20022 external code set.
External code sets can be downloaded from www.iso20022.org.
*`PCED`-The parties have fulfilled all liabilities under the contract (loan agreement), including fulfillment of the liabilities by a resident third party (by another resident party).
*`POTR`-If the liabilities under the contract (loan agreement) are fulfilled (stopped) on other grounds, not mentioned in the currency control regulation.
*`PRNR`-At the termination of the grounds (under the regulation) require the registered contract to be issued, including the cases resulting from making the appropriate changes and (or) additions to the contract (loan agreement), or if the registered contract has been wrongly issued in the absence in the contract (loan agreement) of any grounds for its issuance.
*`PSBT`-The resident cedes a claim under the contract (loan agreement) to another resident  party, or transfers a debt under the contract (loan agreement) to another resident  party.
*`PSNR`-The resident cedes a claim under the contract (loan agreement) to a non-resident.
*`PTAA`-The registered contract has been transferred from the bank together with the transfer of the underlying contract (loan agreement) for servicing to another authorised bank (to another affiliate of this authorised bank, from the head office to an affiliate of this authorised bank, or from an affiliate to the head office of this authorised bank), as well as if the resident closes all settlement accounts in the bank of the registered contract.
*`RACC`-All customer's accounts are closed: In the case the resident closes all settlement accounts at the bank where the contract was registered  without closing the registered contract according to the regulation, the bank  shall be entitled to independently close the registered contract after the expiration of 30 working days following the date of closing of the settlement account (last settlement account) of the resident.
*`RCED`-If the bank has all information available for the closing of the registered contract, and all liabilities under the contract (loan agreement) have been fulfilled (terminated), while the resident has not filled an application for closing the registered contract.
*`REXP`-In case of failure (on the basis of the information available in the registered contracts data base at the bank) of all obligations under the contract (loan agreement), and failure to provide by a resident of the documents and information (under the regulation), based on which the registered agent conducts a statement of banking supervision, within 180 calendar days following the date specified in the specified section (for example column 6 of Section 3 for Russia) of the registered contract.
In the case referred to in this paragraph, the bank informs  (at its discretion) the resident about the closure of the registered contract not later than in two working days after the date of its closure.

## Source constraints

```json
{
  "type": "string",
  "minLength": 1,
  "maxLength": 4
}
```

## Complete enumeration

| Position | Exact code |
| --- | --- |
| 1 | PCED |
| 2 | POTR |
| 3 | PRNR |
| 4 | PSBT |
| 5 | PSNR |
| 6 | PTAA |
| 7 | RACC |
| 8 | RCED |
| 9 | REXP |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
